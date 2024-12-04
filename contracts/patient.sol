pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title ContractPatient
 * @dev Manages patient registration and basic information
 */
contract ContractPatient is AccessControl, Pausable, ReentrancyGuard {
    bytes32 public constant ADMIN_ROLE = keccak256("ADMIN_ROLE");
    bytes32 public constant PATIENT_ROLE = keccak256("PATIENT_ROLE");

    struct PatientInfo {
        string name;
        bool gender;
        string dateOfBirth;
        string contactInfo;
        string bloodType;
        bytes32[] medicalRecords;
        bool isRegistered;
    }

    mapping(address => PatientInfo) private patients;

    event PatientRegistered(address indexed patientAddress, string name);
    event PatientInfoUpdated(address indexed patientAddress);

    constructor() {
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(ADMIN_ROLE, msg.sender);
    }

    /**
     * @dev Register a new patient
     */
    function registerPatient(
        string memory name,
        bool memory gender,
        string memory dateOfBirth, 
        string memory contactInfo
    ) external whenNotPaused nonReentrant {
        require(!patients[msg.sender].isRegistered, "Patient already registered");
        
        patients[msg.sender] = PatientInfo({
            name: name,
            gender: gender,
            dateOfBirth: dateOfBirth,
            contactInfo: contactInfo,
            bloodType: "",
            medicalRecordHash: "",
            isRegistered: true
        });

        _grantRole(PATIENT_ROLE, msg.sender);
        emit PatientRegistered(msg.sender, name);
    }

    /**
     * @dev Update patient information
     */
    function updatePatientInfo(
        string memory name, 
        string memory contactInfo
    ) external whenNotPaused nonReentrant {
        require(patients[msg.sender].isRegistered, "Patient not registered");
        
        patients[msg.sender].name = name;
        patients[msg.sender].contactInfo = contactInfo;
        
        emit PatientInfoUpdated(msg.sender);
    }

    /**
     * @dev Link medical record hash
     */
    function linkMedicalRecord(bytes32 medicalRecordHash) external {
        require(patients[msg.sender].isRegistered, "Patient not registered");
        patients[msg.sender].medicalRecords.push(medicalRecordHash);
    }

    /**
     * @dev Get patient information
     */
    function getPatientInfo() external view returns (PatientInfo memory) {
        require(patients[msg.sender].isRegistered, "Patient not registered");
        return patients[msg.sender];
    }

    function pause() external onlyRole(ADMIN_ROLE) {
        _pause();
    }

    function unpause() external onlyRole(ADMIN_ROLE) {
        _unpause();
    }
}
