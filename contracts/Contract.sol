// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// AUDIT CONTRACT
contract AuditContract {
    struct AuditRecord {
        address actor;
        address subject;
        string action;
        string details;
        uint256 timestamp;
        bytes32 transactionHash;
    }
    
    AuditRecord[] public auditTrail;
    mapping(address => uint256[]) private actorAudits;
    mapping(address => uint256[]) private subjectAudits;
    
    event AuditEvent(
        address indexed actor,
        address indexed subject,
        string action,
        string details,
        uint256 timestamp,
        bytes32 transactionHash
    );
    
    function recordEvent(
        address _actor,
        address _subject,
        string memory _action,
        string memory _details
    ) external {
        uint256 recordId = auditTrail.length;
        bytes32 txHash = blockhash(block.number - 1);
        
        AuditRecord memory newRecord = AuditRecord({
            actor: _actor,
            subject: _subject,
            action: _action,
            details: _details,
            timestamp: block.timestamp,
            transactionHash: txHash
        });
        
        auditTrail.push(newRecord);
        actorAudits[_actor].push(recordId);
        subjectAudits[_subject].push(recordId);
        
        emit AuditEvent(_actor, _subject, _action, _details, block.timestamp, txHash);
    }
    
    function getAuditTrail() external view returns (AuditRecord[] memory) {
        return auditTrail;
    }
    
    function getActorAudits(address _actor) external view returns (AuditRecord[] memory) {
        uint256[] memory recordIds = actorAudits[_actor];
        AuditRecord[] memory records = new AuditRecord[](recordIds.length);
        
        for (uint256 i = 0; i < recordIds.length; i++) {
            records[i] = auditTrail[recordIds[i]];
        }
        
        return records;
    }
    
    function getSubjectAudits(address _subject) external view returns (AuditRecord[] memory) {
        uint256[] memory recordIds = subjectAudits[_subject];
        AuditRecord[] memory records = new AuditRecord[](recordIds.length);
        
        for (uint256 i = 0; i < recordIds.length; i++) {
            records[i] = auditTrail[recordIds[i]];
        }
        
        return records;
    }
}

// PATIENT CONTRACT
contract PatientContract is ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _patientIds;
    
    AuditContract private auditContract;
    
    struct Patient {
        uint256 id;
        string fullName;
        string dateOfBirth;
        string phoneNumber;
        string gender;
        address patientAddress;
        bool isRegistered;
        bool isActive;
        mapping(address => bool) authorizedDoctors;
    }
    
    struct PatientLogin {
        bytes32 privateKeyHash;
        uint256 lastLoginTimestamp;
        uint256 loginAttempts;
    }
    
    mapping(address => Patient) public patients;
    mapping(address => PatientLogin) private patientLogins;
    mapping(string => bool) private usedPrivateKeys;
    mapping(string => address) private phoneToAddress;
    address[] public allPatientAddresses;
    address private admin;
    
    // Events
    event PatientRegistered(
        address indexed patientAddress, 
        uint256 patientId, 
        string fullName,
        string privateKey
    );
    event PatientLoggedIn(address indexed patientAddress, uint256 timestamp);
    event AccessGranted(address indexed patientAddress, address indexed doctorAddress);
    event AccessRevoked(address indexed patientAddress, address indexed doctorAddress);
    event PatientDeactivated(address indexed patientAddress);
    event PatientReactivated(address indexed patientAddress);
    
    // Modifiers
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }
    
    modifier onlyRegisteredPatient() {
        require(patients[msg.sender].isRegistered, "Patient not registered");
        require(patients[msg.sender].isActive, "Patient account is not active");
        _;
    }
    
    constructor(address _auditContractAddress) {
        admin = msg.sender;
        auditContract = AuditContract(_auditContractAddress);
    }
    
    // Patient Registration
    function registerPatient(
        string memory _fullName,
        string memory _dateOfBirth,
        string memory _phoneNumber,
        string memory _gender,
        string memory _privateKey
    ) external nonReentrant returns (string memory) {
        require(!patients[msg.sender].isRegistered, "Patient already registered");
        require(!usedPrivateKeys[_privateKey], "Private key already used");
        require(phoneToAddress[_phoneNumber] == address(0), "Phone number already registered");
        
        // Generate patient ID
        _patientIds.increment();
        uint256 newPatientId = _patientIds.current();
        
        // Create patient struct
        Patient storage newPatient = patients[msg.sender];
        newPatient.id = newPatientId;
        newPatient.fullName = _fullName;
        newPatient.dateOfBirth = _dateOfBirth;
        newPatient.phoneNumber = _phoneNumber;
        newPatient.gender = _gender;
        newPatient.patientAddress = msg.sender;
        newPatient.isRegistered = true;
        newPatient.isActive = true;
        
        // Store login information
        patientLogins[msg.sender] = PatientLogin({
            privateKeyHash: keccak256(abi.encodePacked(_privateKey)),
            lastLoginTimestamp: 0,
            loginAttempts: 0
        });
        
        // Mark private key as used and associate phone number
        usedPrivateKeys[_privateKey] = true;
        phoneToAddress[_phoneNumber] = msg.sender;
        allPatientAddresses.push(msg.sender);
        
        // Record audit event
        auditContract.recordEvent(
            msg.sender, 
            msg.sender, 
            "Patient Registration", 
            string(abi.encodePacked("Patient ", _fullName, " registered"))
        );
        
        // Emit registration event with private key
        emit PatientRegistered(msg.sender, newPatientId, _fullName, _privateKey);
        
        return _privateKey;
    }
    
    // Patient Login
    function loginPatient(string memory _privateKey) external returns (bool) {
        require(patients[msg.sender].isRegistered, "Patient not registered");
        require(patients[msg.sender].isActive, "Patient account is not active");
        
        PatientLogin storage loginInfo = patientLogins[msg.sender];
        
        // Check if private key matches
        require(
            loginInfo.privateKeyHash == keccak256(abi.encodePacked(_privateKey)),
            "Invalid private key"
        );
        
        // Reset login attempts
        loginInfo.loginAttempts = 0;
        loginInfo.lastLoginTimestamp = block.timestamp;
        
        // Record audit event
        auditContract.recordEvent(
            msg.sender, 
            msg.sender, 
            "Patient Login", 
            "Patient logged in successfully"
        );
        
        emit PatientLoggedIn(msg.sender, block.timestamp);
        return true;
    }
    
    // Access Management
    function grantAccess(address _doctorAddress) external onlyRegisteredPatient {
        patients[msg.sender].authorizedDoctors[_doctorAddress] = true;
        
        // Record audit event
        auditContract.recordEvent(
            msg.sender, 
            _doctorAddress, 
            "Doctor Access Granted", 
            "Patient granted access to doctor"
        );
        
        emit AccessGranted(msg.sender, _doctorAddress);
    }
    
    function revokeAccess(address _doctorAddress) external onlyRegisteredPatient {
        patients[msg.sender].authorizedDoctors[_doctorAddress] = false;
        
        // Record audit event
        auditContract.recordEvent(
            msg.sender, 
            _doctorAddress, 
            "Doctor Access Revoked", 
            "Patient revoked access from doctor"
        );
        
        emit AccessRevoked(msg.sender, _doctorAddress);
    }
    
    function checkAccess(address _patientAddress, address _doctorAddress) external view returns (bool) {
        return patients[_patientAddress].authorizedDoctors[_doctorAddress];
    }
    
    // Account Management
    function deactivatePatient(address _patientAddress) external onlyAdmin {
        require(patients[_patientAddress].isRegistered, "Patient not registered");
        require(patients[_patientAddress].isActive, "Patient already deactivated");
        patients[_patientAddress].isActive = false;
        
        // Record audit event
        auditContract.recordEvent(
            msg.sender, 
            _patientAddress, 
            "Patient Deactivation", 
            "Patient account deactivated"
        );
        
        emit PatientDeactivated(_patientAddress);
    }
    
    function reactivatePatient(address _patientAddress) external onlyAdmin {
        require(patients[_patientAddress].isRegistered, "Patient not registered");
        require(!patients[_patientAddress].isActive, "Patient already active");
        patients[_patientAddress].isActive = true;
        
        // Record audit event
        auditContract.recordEvent(
            msg.sender, 
            _patientAddress, 
            "Patient Reactivation", 
            "Patient account reactivated"
        );
        
        emit PatientReactivated(_patientAddress);
    }
    
    // Utility Functions
    function getPatientDetails(address _patientAddress) 
        external 
        view 
        returns (
            uint256 id,
            string memory fullName,
            string memory dateOfBirth,
            string memory phoneNumber,
            string memory gender,
            bool isActive
        ) 
    {
        Patient storage patient = patients[_patientAddress];
        return (
            patient.id,
            patient.fullName,
            patient.dateOfBirth,
            patient.phoneNumber,
            patient.gender,
            patient.isActive
        );
    }
    
    function isPatientRegistered(address _address) public view returns (bool) {
        return patients[_address].isRegistered;
    }
    
    function getPatientCount() public view returns (uint256) {
        return allPatientAddresses.length;
    }
    
    function getAllPatients() public view returns (address[] memory) {
        return allPatientAddresses;
    }
}

// DOCTOR CONTRACT
contract DoctorContract is ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _doctorIds;
    Counters.Counter private _fileIds;
    
    AuditContract private auditContract;
    PatientContract private patientContract;
    
    struct Doctor {
        uint256 id;
        string fullName;
        string dateOfBirth;
        string phoneNumber;
        string gender;
        string speciality;
        address doctorAddress;
        string licenseNumber;
        bool isRegistered;
        bool isActive;
    }
    
    struct DoctorLogin {
        bytes32 privateKeyHash;
        uint256 lastLoginTimestamp;
        uint256 loginAttempts;
    }
    
    struct MedicalFile {
        uint256 fileId;
        string ipfsHash;
        string encryptedKey;
        string fileName;
        string fileType;
        string comment;
        uint256 timestamp;
        address doctorAddress;
        bool isActive;
        string diagnosis;
        string prescription;
    }
    
    mapping(address => Doctor) public doctors;
    mapping(address => DoctorLogin) private doctorLogins;
    mapping(address => MedicalFile[]) private patientFiles;
    mapping(uint256 => address) private fileToPatient;
    mapping(string => bool) private usedPrivateKeys;
    mapping(string => bool) private usedLicenseNumbers;
    mapping(string => address) private phoneToAddress;
    address[] public allDoctorAddresses;
    address private admin;
    
    // Events
    event DoctorRegistered(
        address indexed doctorAddress, 
        uint256 doctorId, 
        string fullName,
        string privateKey
    );
    event DoctorLoggedIn(address indexed doctorAddress, uint256 timestamp);
    event FileUploaded(
        uint256 indexed fileId,
        address indexed patientAddress,
        address indexed doctorAddress,
        string ipfsHash,
        string fileName,
        uint256 timestamp
    );
    event FileUpdated(uint256 indexed fileId, string newComment);
    
    // Modifiers
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }
    
    modifier onlyRegisteredDoctor() {
        require(doctors[msg.sender].isRegistered, "Doctor not registered");
        require(doctors[msg.sender].isActive, "Doctor account is not active");
        _;
    }
    
    constructor(address _patientContractAddress, address _auditContractAddress) {
        admin = msg.sender;
        patientContract = PatientContract(_patientContractAddress);
        auditContract = AuditContract(_auditContractAddress);
    }
    
    // Doctor Registration
    function registerDoctor(
        string memory _fullName,
        string memory _dateOfBirth,
        string memory _phoneNumber,
        string memory _gender,
        string memory _speciality,
        string memory _licenseNumber,
        string memory _privateKey
    ) external nonReentrant returns (string memory) {
        require(!doctors[msg.sender].isRegistered, "Doctor already registered");
        require(!usedPrivateKeys[_privateKey], "Private key already used");
        require(!usedLicenseNumbers[_licenseNumber], "License number already registered");
        require(phoneToAddress[_phoneNumber] == address(0), "Phone number already registered");
        
        // Generate doctor ID
        _doctorIds.increment();
        uint256 newDoctorId = _doctorIds.current();
        
        // Create doctor struct
        doctors[msg.sender] = Doctor({
            id: newDoctorId,
            fullName: _fullName,
            dateOfBirth: _dateOfBirth,
            phoneNumber: _phoneNumber,
            gender: _gender,
            speciality: _speciality,
            doctorAddress: msg.sender,
            licenseNumber: _licenseNumber,
            isRegistered: true,
            isActive: true
        });
        
        // Store login information
        doctorLogins[msg.sender] = DoctorLogin({
            privateKeyHash: keccak256(abi.encodePacked(_privateKey)),
            lastLoginTimestamp: 0,
            loginAttempts: 0
        });
        
  
        usedPrivateKeys[_privateKey] = true;
        usedLicenseNumbers[_licenseNumber] = true;
        phoneToAddress[_phoneNumber] = msg.sender;
        allDoctorAddresses.push(msg.sender);
        
        emit DoctorRegistered(msg.sender, newDoctorId, _fullName, _privateKey);
        
        return "Doctor registered successfully";
    }
    
    // Doctor Login
    function doctorLogin(string memory _privateKey) external nonReentrant {
        require(doctors[msg.sender].isRegistered, "Doctor not registered");
        require(doctors[msg.sender].isActive, "Doctor account is not active");
        
        // Check private key match
        bytes32 privateKeyHash = keccak256(abi.encodePacked(_privateKey));
        require(privateKeyHash == doctorLogins[msg.sender].privateKeyHash, "Invalid private key");
        
        // Update login timestamp and reset login attempts
        doctorLogins[msg.sender].lastLoginTimestamp = block.timestamp;
        doctorLogins[msg.sender].loginAttempts = 0;
        
        emit DoctorLoggedIn(msg.sender, block.timestamp);
    }

    // File Management: Uploading a Medical File
    function uploadMedicalFile(
        address _patientAddress,
        string memory _ipfsHash,
        string memory _encryptedKey,
        string memory _fileName,
        string memory _fileType,
        string memory _comment,
        string memory _diagnosis,
        string memory _prescription
    ) 
        external 
        onlyRegisteredDoctor
    {
        require(patientContract.checkAccess(_patientAddress, msg.sender), "No access to patient's data");

        _fileIds.increment();
        uint256 newFileId = _fileIds.current();
        
        MedicalFile memory newFile = MedicalFile({
            fileId: newFileId,
            ipfsHash: _ipfsHash,
            encryptedKey: _encryptedKey,
            fileName: _fileName,
            fileType: _fileType,
            comment: _comment,
            timestamp: block.timestamp,
            doctorAddress: msg.sender,
            isActive: true,
            diagnosis: _diagnosis,
            prescription: _prescription
        });

        patientFiles[_patientAddress].push(newFile);
        fileToPatient[newFileId] = _patientAddress;

        emit FileUploaded(newFileId, _patientAddress, msg.sender, _ipfsHash, _fileName, block.timestamp);
    }

    // Update Medical File Details
    function updateFileDetails(
        uint256 _fileId,
        string memory _newComment,
        string memory _newDiagnosis,
        string memory _newPrescription
    )
        external 
        onlyRegisteredDoctor
    {
        address patientAddress = fileToPatient[_fileId];
        require(patientAddress != address(0), "File not found");
        require(patientContract.checkAccess(patientAddress, msg.sender), "No access to this file");
        
        // Find and update the file in the patient's record
        for (uint i = 0; i < patientFiles[patientAddress].length; i++) {
            if (patientFiles[patientAddress][i].fileId == _fileId) {
                patientFiles[patientAddress][i].comment = _newComment;
                patientFiles[patientAddress][i].diagnosis = _newDiagnosis;
                patientFiles[patientAddress][i].prescription = _newPrescription;
                emit FileUpdated(_fileId, _newComment);
                break;
            }
        }
    }

    // Admin Functions to deactivate/reactivate doctors
    function deactivateDoctor(address _doctorAddress) external onlyAdmin {
        require(doctors[_doctorAddress].isRegistered, "Doctor not registered");
        require(doctors[_doctorAddress].isActive, "Doctor already deactivated");

        doctors[_doctorAddress].isActive = false;
    }

    function reactivateDoctor(address _doctorAddress) external onlyAdmin {
        require(doctors[_doctorAddress].isRegistered, "Doctor not registered");
        require(!doctors[_doctorAddress].isActive, "Doctor already active");

        doctors[_doctorAddress].isActive = true;
    }

    // View functions for doctor and file information
    function getDoctorDetails(address _doctorAddress)
        external 
        view 
        returns (
            uint256 id, 
            string memory fullName, 
            string memory speciality, 
            bool isActive
        )
    {
        Doctor memory doctor = doctors[_doctorAddress];
        return (doctor.id, doctor.fullName, doctor.speciality, doctor.isActive);
    }

    function getPatientFiles(address _patientAddress) 
        external 
        view 
        returns (MedicalFile[] memory)
    {
        return patientFiles[_patientAddress];
    }

    function getFileDetails(uint256 _fileId) 
        external 
        view 
        returns (MedicalFile memory)
    {
        address patientAddress = fileToPatient[_fileId];
        require(patientAddress != address(0), "File does not exist");

        for (uint i = 0; i < patientFiles[patientAddress].length; i++) {
            if (patientFiles[patientAddress][i].fileId == _fileId) {
                return patientFiles[patientAddress][i];
            }
        }
        revert("File not found");
    }
}