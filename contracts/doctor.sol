// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "./patient.sol";
import "./audit.sol";

contract ContractDoctor is AccessControl, Pausable, ReentrancyGuard {
    bytes32 public constant ADMIN_ROLE = keccak256("ADMIN_ROLE");
    bytes32 public constant DOCTOR_ROLE = keccak256("DOCTOR_ROLE");
    bytes32 public constant HOSPITAL_ROLE = keccak256("HOSPITAL_ROLE");

    struct AccessControl {
        bool accessGranted;
        uint256 expirationTime;
    }

    mapping(address => mapping(address => AccessControl)) private patientToDoctorAccess;
    mapping(address => mapping(address => bool)) private delegatedAccess;

    ContractPatient private contractPatient;
    ContractAudit private contractAudit;

    event DoctorRegistered(address indexed doctorAddress, string name, string specialty);
    event AccessGranted(address indexed patient, address indexed doctor, uint256 expirationTime);
    event AccessRevoked(address indexed patient, address indexed doctor);
    event EmergencyAccessUsed(address indexed doctor, address indexed patient, string justification);

    constructor(address patientContractAddress, address auditContractAddress) {
        contractPatient = ContractPatient(patientContractAddress);
        contractAudit = ContractAudit(auditContractAddress);
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(ADMIN_ROLE, msg.sender);
    }

    modifier onlyDoctor() {
        require(hasRole(DOCTOR_ROLE, msg.sender), "Caller is not a doctor");
        _;
    }

    modifier onlyPatient(address patientAddress) {
        require(contractPatient.hasRole(PATIENT_ROLE, patientAddress), "Caller is not registered as a patient");
        require(msg.sender == patientAddress, "Only patient can perform this action");
        _;
    }

    function registerDoctor(
        string memory name, 
        string memory specialty
    ) external whenNotPaused nonReentrant {
        require(!hasRole(DOCTOR_ROLE, msg.sender), "Doctor already registered");

        _grantRole(DOCTOR_ROLE, msg.sender);
        emit DoctorRegistered(msg.sender, name, specialty);
    }

    function grantAccess(address doctorAddress, uint256 durationInHours) external whenNotPaused nonReentrant onlyPatient(msg.sender) {
        require(hasRole(DOCTOR_ROLE, doctorAddress), "Address is not a doctor");
        uint256 expirationTime = block.timestamp + (durationInHours * 1 hours);
        patientToDoctorAccess[msg.sender][doctorAddress] = AccessControl(true, expirationTime);
        emit AccessGranted(msg.sender, doctorAddress, expirationTime);
        contractAudit.logAction(msg.sender, "Access Granted to Doctor", block.timestamp);
    }

    function revokeAccess(address doctorAddress) external whenNotPaused nonReentrant onlyPatient(msg.sender) {
        require(patientToDoctorAccess[msg.sender][doctorAddress].accessGranted, "No access to revoke");
        delete patientToDoctorAccess[msg.sender][doctorAddress];
        emit AccessRevoked(msg.sender, doctorAddress);
        contractAudit.logAction(msg.sender, "Access Revoked from Doctor", block.timestamp);
    }

    function checkAccess(address patientAddress, address doctorAddress) external view returns (bool) {
        AccessControl memory access = patientToDoctorAccess[patientAddress][doctorAddress];
        if (access.accessGranted && access.expirationTime > block.timestamp) {
            return true;
        }
        return false;
    }

    function emergencyAccess(address patientAddress, string memory justification) external whenNotPaused nonReentrant onlyDoctor {
        emit EmergencyAccessUsed(msg.sender, patientAddress, justification);
        contractAudit.logAction(patientAddress, "Emergency Access Used by Doctor", block.timestamp);
    }

    function delegateAccess(address fromDoctor, address toDoctor, address patientAddress) 
        external 
        whenNotPaused 
        nonReentrant 
        onlyPatient(patientAddress) 
    {
        require(hasRole(DOCTOR_ROLE, fromDoctor) && hasRole(DOCTOR_ROLE, toDoctor), "Invalid doctor addresses");
        require(checkAccess(patientAddress, fromDoctor), "Original doctor has no access");

        delegatedAccess[patientAddress][toDoctor] = true;
        emit AccessDelegated(fromDoctor, toDoctor, patientAddress);
    }

    function revokeDelegatedAccess(address fromDoctor, address toDoctor, address patientAddress) 
        external 
        whenNotPaused 
        nonReentrant 
        onlyPatient(patientAddress) 
    {
        require(delegatedAccess[patientAddress][toDoctor], "No delegated access to revoke");

        delegatedAccess[patientAddress][toDoctor] = false;
        emit DelegatedAccessRevoked(fromDoctor, toDoctor, patientAddress);
    }
}