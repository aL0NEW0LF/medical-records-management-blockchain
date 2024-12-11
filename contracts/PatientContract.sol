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
    
    // Mappings
    mapping(address => Patient) public patients;
    mapping(address => mapping(address => DoctorAccess)) public patientDoctorAccess;
    mapping(address => string[]) public patientMedicalFiles;
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
    
    // Grant Access to Doctor
    function grantDoctorAccess(address _doctorAddress) external nonReentrant {
        require(patients[msg.sender].isRegistered, "Patient not registered");
        
        patientDoctorAccess[msg.sender][_doctorAddress] = DoctorAccess({
            doctorAddress: _doctorAddress,
            hasAccess: true
        });
        
        emit DoctorAccessGranted(msg.sender, _doctorAddress);
    }
    
    // Revoke Doctor Access
    function revokeDoctorAccess(address _doctorAddress) external nonReentrant {
        require(patients[msg.sender].isRegistered, "Patient not registered");
        
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
    function addMedicalFile(string memory _ipfsHash) external nonReentrant {
        require(patients[msg.sender].isRegistered, "Patient not registered");
        
        patientMedicalFiles[msg.sender].push(_ipfsHash);
        
        emit MedicalFileAdded(msg.sender, _ipfsHash);
    }
    
    // Add Comment
    function addComment(string memory _comment) external nonReentrant {
        require(patients[msg.sender].isRegistered, "Patient not registered");
        
        patientComments[msg.sender].push(_comment);
        
        emit CommentAdded(msg.sender, _comment);
    }
    
    // Get Patient Information (only for patients with granted access)
    function getPatientInfo(address _patientAddress) 
        external 
        view 
        returns (Patient memory) 
    {
        require(
            patientDoctorAccess[_patientAddress][msg.sender].hasAccess, 
            "No access to patient information"
        );
        return patients[_patientAddress];
    }
    
    // Get Medical Files
    function getMedicalFiles(address _patientAddress) 
        external 
        view 
        returns (string[] memory) 
    {
        require(
            patientDoctorAccess[_patientAddress][msg.sender].hasAccess, 
            "No access to patient files"
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