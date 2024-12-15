// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract PatientContract is ReentrancyGuard {
    using Counters for Counters.Counter;
    
    // Patient Structure
    struct Patient {
        address patientAddress;
        string fullName;
        string dateOfBirth;
        string phoneNumber;
        string gender;
        bool isRegistered;
    }
    
    // Access Control Structure
    struct DoctorAccess {
        address doctorAddress;
        bool hasAccess;
    }
    
    struct MedicalFile {
        string ipfsHash;
        string name;
    }

    // Mappings
    mapping(address => Patient) public patients;
    mapping(address => mapping(address => DoctorAccess)) public patientDoctorAccess;
    mapping(address => MedicalFile[]) public patientMedicalFiles;
    mapping(address => string[]) public patientComments;
    
    // Counters
    Counters.Counter private patientCounter;
    
    // Events
    event PatientRegistered(address indexed patientAddress, string fullName);
    event DoctorAccessGranted(address indexed patientAddress, address indexed doctorAddress);
    event DoctorAccessRevoked(address indexed patientAddress, address indexed doctorAddress);
    event MedicalFileAdded(address indexed patientAddress, string ipfsHash);
    event CommentAdded(address indexed patientAddress, string comment);
    
    // Patient Registration
    function registerPatient(
        string memory _fullName, 
        string memory _dateOfBirth, 
        string memory _phoneNumber, 
        string memory _gender
    ) external nonReentrant {
        require(!patients[msg.sender].isRegistered, "Patient already registered");
        
        patients[msg.sender] = Patient({
            patientAddress: msg.sender,
            fullName: _fullName,
            dateOfBirth: _dateOfBirth,
            phoneNumber: _phoneNumber,
            gender: _gender,
            isRegistered: true
        });
        
        patientCounter.increment();
        
        emit PatientRegistered(msg.sender, _fullName);
    }
    
    function isPatientRegistered(address _patientAddress) external view returns (bool) {
        return patients[_patientAddress].isRegistered;
    }

    // Grant Access to Doctor
    function grantDoctorAccess(address _doctorAddress) external nonReentrant {
        require(patients[msg.sender].isRegistered, "Patient not registered");
        require(!patientDoctorAccess[msg.sender][_doctorAddress].hasAccess, "Doctor already has access");
        
        patientDoctorAccess[msg.sender][_doctorAddress] = DoctorAccess({
            doctorAddress: _doctorAddress,
            hasAccess: true
        });
        
        emit DoctorAccessGranted(msg.sender, _doctorAddress);
    }
    
    // Revoke Doctor Access
    function revokeDoctorAccess(address _doctorAddress) external nonReentrant {
        require(patients[msg.sender].isRegistered, "Patient not registered");
        require(patientDoctorAccess[msg.sender][_doctorAddress].hasAccess, "Doctor does not have access");

        delete patientDoctorAccess[msg.sender][_doctorAddress];
        
        emit DoctorAccessRevoked(msg.sender, _doctorAddress);
    }
    
    // New method to check doctor access (external visibility)
    function checkDoctorAccess(address _patientAddress, address _doctorAddress) 
        external 
        view 
        returns (bool) 
    {
        return patientDoctorAccess[_patientAddress][_doctorAddress].hasAccess;
    }
    
    // Add Medical File
    function addMedicalFile(string memory _ipfsHash, string memory name, address _patientAddress) external nonReentrant {
        require(patients[_patientAddress].isRegistered, "Patient not registered");
        
        patientMedicalFiles[_patientAddress].push(MedicalFile({
            ipfsHash: _ipfsHash,
            name: name
        }));
        
        emit MedicalFileAdded(_patientAddress, _ipfsHash);
    }

    function deleteMedicalFile(string memory _ipfsHash) external nonReentrant {
        require(patients[msg.sender].isRegistered, "Patient not registered");
        
        MedicalFile[] storage files = patientMedicalFiles[msg.sender];
        for (uint i = 0; i < files.length; i++) {
            if (keccak256(abi.encodePacked(files[i].ipfsHash)) == keccak256(abi.encodePacked(_ipfsHash))) {
                for (uint j = i; j < files.length - 1; j++) {
                    files[j] = files[j + 1];
                }
                files.pop();
                break;
            }
        }
    }
    
    // Add Comment
    function addComment(string memory _comment) external nonReentrant {
        require(patients[msg.sender].isRegistered, "Patient not registered");
        
        patientComments[msg.sender].push(_comment);
        
        emit CommentAdded(msg.sender, _comment);
    }
    
    // Get Own Patient Information
    function getPatientInfo() 
        external 
        view 
        returns (string memory, string memory, string memory, string memory)
    {
        require(patients[msg.sender].isRegistered, "Patient not registered");
        return (
            patients[msg.sender].fullName, 
            patients[msg.sender].dateOfBirth, 
            patients[msg.sender].phoneNumber, 
            patients[msg.sender].gender
        );
    }
    
    function getOwnMedicalFiles() external view returns (MedicalFile[] memory) {
        require(patients[msg.sender].isRegistered, "Patient not registered");
        return patientMedicalFiles[msg.sender];
    }

    // Get Medical Files
    function getMedicalFiles(address _patientAddress, address _doctorAddress) 
        external 
        view 
        returns (MedicalFile[] memory)
    {
        require(patients[_patientAddress].isRegistered, "Patient not registered");
        require(
            patientDoctorAccess[_patientAddress][_doctorAddress].hasAccess, 
            "No access to patient medical files"
        );
        return patientMedicalFiles[_patientAddress];
    }
    
    // Get Patient Comments
    function getComments(address _patientAddress) 
        external 
        view 
        returns (string[] memory) 
    {
        require(
            patientDoctorAccess[_patientAddress][msg.sender].hasAccess, 
            "No access to patient comments"
        );
        return patientComments[_patientAddress];
    }
    
    // Get Total Registered Patients
    function getTotalPatients() external view returns (uint256) {
        return patientCounter.current();
    }
}