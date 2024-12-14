// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "./PatientContract.sol";

contract DoctorContract is ReentrancyGuard {
    using Counters for Counters.Counter;
    
    // Doctor Structure
    struct Doctor {
        address doctorAddress;
        string fullName;
        string dateOfBirth;
        string phoneNumber;
        string gender;
        string speciality;
        string licenseNumber;
        bool isRegistered;
    }
    
    // Patient Contract Reference
    PatientContract public patientContract;
    
    // Mappings
    mapping(address => Doctor) public doctors;
    mapping(address => string[]) public doctorMedicalFiles;
    
    // Counters
    Counters.Counter private doctorCounter;
    
    // Events
    event DoctorRegistered(address indexed doctorAddress, string fullName, string speciality);
    event MedicalFileUploaded(address indexed doctorAddress, address indexed patientAddress, string ipfsHash);
    
    // Constructor
    constructor(address _patientContractAddress) {
        patientContract = PatientContract(_patientContractAddress);
    }
    
    // Doctor Registration
    function registerDoctor(
        string memory _fullName,
        string memory _dateOfBirth,
        string memory _phoneNumber,
        string memory _gender,
        string memory _speciality,
        string memory _licenseNumber
    ) external nonReentrant {
        require(!doctors[msg.sender].isRegistered, "Doctor already registered");
        
        doctors[msg.sender] = Doctor({
            doctorAddress: msg.sender,
            fullName: _fullName,
            dateOfBirth: _dateOfBirth,
            phoneNumber: _phoneNumber,
            gender: _gender,
            speciality: _speciality,
            licenseNumber: _licenseNumber,
            isRegistered: true
        });
        
        doctorCounter.increment();
        
        emit DoctorRegistered(msg.sender, _fullName, _speciality);
    }
    
    // Upload Medical File for a Patient
    function uploadMedicalFile(
        address _patientAddress, 
        string memory name,
        string memory _ipfsHash
    ) external nonReentrant {
        // Check if doctor is registered
        require(doctors[msg.sender].isRegistered, "Doctor not registered");
        
        // Check if doctor has access to patient
        require(
            patientContract.checkDoctorAccess(_patientAddress, msg.sender), 
            "No access to patient"
        );
        
        // Add file to patient's medical files via patient contract
        patientContract.addMedicalFile(name, _ipfsHash);
        
        // Track doctor's uploaded files
        doctorMedicalFiles[msg.sender].push(_ipfsHash);
        
        emit MedicalFileUploaded(msg.sender, _patientAddress, _ipfsHash);
    }
    
    // Get Doctor Information
    function getDoctorInfo(address _doctorAddress) 
        external 
        view 
        returns (string memory, string memory, string memory, string memory, string memory, string memory)
    {
        return (
            doctors[_doctorAddress].fullName, 
            doctors[_doctorAddress].dateOfBirth, 
            doctors[_doctorAddress].phoneNumber, 
            doctors[_doctorAddress].gender,
            doctors[_doctorAddress].speciality,
            doctors[_doctorAddress].licenseNumber
        );
    }

    function getPatientMedicalFiles(address _patientAddress) 
        external 
        view 
        returns (PatientContract.MedicalFile[] memory) 
    {
        require(
            patientContract.checkDoctorAccess(_patientAddress, msg.sender), 
            "No access to patient"
        );

        return patientContract.getMedicalFiles(_patientAddress);
    }

    // Get Doctor's Uploaded Medical Files
    function getDoctorMedicalFiles() 
        external 
        view 
        returns (string[] memory) 
    {
        return doctorMedicalFiles[msg.sender];
    }
    
    // Get Total Registered Doctors
    function getTotalDoctors() external view returns (uint256) {
        return doctorCounter.current();
    }
}