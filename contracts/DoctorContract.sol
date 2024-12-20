// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "./PatientContract.sol";
import "./RoleContract.sol";

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

    struct MedicalFile {
        string ipfsHash;
        string name;
    }

    // Patient Contract Reference
    PatientContract public patientContract;
    
    // Mappings
    mapping(address => Doctor) public doctors;
    mapping(address => MedicalFile[]) public doctorMedicalFiles;
    
    // Counters
    Counters.Counter private doctorCounter;
    
    // Role Contract
    RoleContract public roleContract;

    // Events
    event DoctorRegistered(address indexed doctorAddress, string fullName, string speciality);
    event MedicalFileUploaded(address indexed doctorAddress, address indexed patientAddress, string ipfsHash);
    
    // Constructor
    constructor(address _patientContractAddress, address _roleContractAddress) {
        patientContract = PatientContract(_patientContractAddress);
        roleContract = RoleContract(_roleContractAddress);
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
        require(!roleContract.isUserAssigned(msg.sender), "Account already registered as another role");

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
        
        roleContract.assignRole(msg.sender, 2);
        doctorCounter.increment();
        
        emit DoctorRegistered(msg.sender, _fullName, _speciality);
    }
    
    function isDoctorRegistered(address _doctorAddress) external view returns (bool) {
        return doctors[_doctorAddress].isRegistered;
    }

    // Upload Medical File for a Patient
    function uploadMedicalFile(
        address _patientAddress, 
        string memory _ipfsHash,
        string memory name
    ) external nonReentrant {
        // Check if doctor is registered
        require(doctors[msg.sender].isRegistered, "Doctor not registered");
        
        // Check if doctor has access to patient
        require(
            patientContract.checkDoctorAccess(_patientAddress, msg.sender), 
            "No access to patient"
        );
        
        // Add file to patient's medical files via patient contract
        patientContract.addMedicalFile(_ipfsHash, name, _patientAddress);
        
        // Track doctor's uploaded files
        doctorMedicalFiles[msg.sender].push(MedicalFile({
            ipfsHash: _ipfsHash,
            name: name
        }));
        
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

        return patientContract.getMedicalFiles(_patientAddress, msg.sender);
    }

    function deleteOwnMedicalFile(string memory _ipfsHash) external nonReentrant {
        require(doctors[msg.sender].isRegistered, "Doctor not registered");
        
        MedicalFile[] storage files = doctorMedicalFiles[msg.sender];
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

    // Get Doctor's Uploaded Medical Files
    function getDoctorMedicalFiles() 
        external 
        view 
        returns (MedicalFile[] memory) 
    {
        return doctorMedicalFiles[msg.sender];
    }
    
    // Get Total Registered Doctors
    function getTotalDoctors() external view returns (uint256) {
        return doctorCounter.current();
    }
}