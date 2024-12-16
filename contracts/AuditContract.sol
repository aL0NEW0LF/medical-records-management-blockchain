// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/utils/Counters.sol";
import "./RoleContract.sol";

contract AuditContract {
    using Counters for Counters.Counter;
    
    // Audit Event Structure
    struct AuditEvent {
        uint256 timestamp;
        address actor;
        string eventType;
        string description;
    }
    
    mapping(address => bool) public auditors;
    address[] registeredAuditors;

    // Mappings
    mapping(uint256 => AuditEvent) public auditTrail;
    Counters.Counter private eventCounter;
    
    // Role Contract
    RoleContract public roleContract;

    // Events
    event EventLogged(
        uint256 indexed eventId, 
        address indexed actor, 
        string eventType, 
        string description
    );
    
    constructor(address _roleContractAddress) {
        roleContract = RoleContract(_roleContractAddress);
        require(!roleContract.isUserAssigned(msg.sender), "Account already registered as another role");
        auditors[msg.sender] = true;
        registeredAuditors.push(msg.sender);
        roleContract.assignRole(msg.sender, 1);
    }

    function isAuditor() public view returns (bool) {
        return auditors[msg.sender];
    }

    function addAuditor(address _auditor) external {
        require(isAuditor(), "Not an auditor");
        require(!auditors[_auditor], "Account is already registered as auditor");
        require(!roleContract.isUserAssigned(_auditor), "Account already registered as another role");
        auditors[_auditor] = true;
        registeredAuditors.push(_auditor);
        roleContract.assignRole(_auditor, 1);
    }

    function getAuditors() external view returns (address[] memory) {
        require(isAuditor(), "Not an auditor");
        return registeredAuditors;
    }

    // Log Patient Registration
    function logPatientRegistration(address _patient, string memory _fullName) external {
        logEvent(_patient, "PATIENT_REGISTRATION", 
            string(abi.encodePacked("Patient Registered: ", _fullName)));
    }
    
    // Log Doctor Registration
    function logDoctorRegistration(address _doctor, string memory _fullName) external {
        logEvent(_doctor, "DOCTOR_REGISTRATION", 
            string(abi.encodePacked("Doctor Registered: ", _fullName)));
    }
    
    // Log Doctor Access Grant
    function logDoctorAccessGrant(
        address _patient, 
        address _doctor
    ) external {
        logEvent(_patient, "DOCTOR_ACCESS_GRANTED", 
            string(abi.encodePacked(
                "Doctor Access Granted: Patient ", 
                addressToString(_patient), 
                " to Doctor ", 
                addressToString(_doctor)
            ))
        );
    }
    
    // Log Doctor Access Revoke
    function logDoctorAccessRevoke(
        address _patient, 
        address _doctor
    ) external {
        logEvent(_patient, "DOCTOR_ACCESS_REVOKED", 
            string(abi.encodePacked(
                "Doctor Access Revoked: Patient ", 
                addressToString(_patient), 
                " from Doctor ", 
                addressToString(_doctor)
            ))
        );
    }
    
    // Log Medical File Upload
    function logDoctorMedicalFileUpload(
        address _doctor, 
        address _patient
    ) external {
        logEvent(_doctor, "MEDICAL_FILE_UPLOAD", 
            string(abi.encodePacked(
                "Medical File Uploaded: Doctor ", 
                addressToString(_doctor), 
                " for Patient ", 
                addressToString(_patient)
            ))
        );
    }

    function logPatientMedicalFileUpload(
        address _patient
    ) external {
        logEvent(_patient, "MEDICAL_FILE_UPLOAD", 
            string(abi.encodePacked(
                "Medical File Uploaded: Patient ", 
                addressToString(_patient)
            ))
        );
    }
    
    // Internal function to log events
    function logEvent(
        address _actor, 
        string memory _eventType, 
        string memory _description
    ) internal {
        uint256 currentEventId = eventCounter.current();
        
        auditTrail[currentEventId] = AuditEvent({
            timestamp: block.timestamp,
            actor: _actor,
            eventType: _eventType,
            description: _description
        });
        
        emit EventLogged(
            currentEventId, 
            _actor, 
            _eventType, 
            _description
        );
        
        eventCounter.increment();
    }
    
    // Utility function to convert address to string
    function addressToString(address _addr) internal pure returns (string memory) {
        bytes32 value = bytes32(uint256(uint160(_addr)));
        bytes memory alphabet = "0123456789abcdef";
        
        bytes memory str = new bytes(42);
        str[0] = '0';
        str[1] = 'x';
        
        for (uint i = 0; i < 20; i++) {
            str[2+i*2] = alphabet[uint(uint8(value[i + 12] >> 4))];
            str[3+i*2] = alphabet[uint(uint8(value[i + 12] & 0x0f))];
        }
        
        return string(str);
    }
    
    // Retrieve Audit Event
    function getAuditEvent(uint256 _eventId) 
        external 
        view 
        returns (AuditEvent memory) 
    {
        require(isAuditor(), "Not an auditor");
        return auditTrail[_eventId];
    }
    
    function getFullAuditTrail() external view returns (AuditEvent[] memory) {
        require(isAuditor(), "Not an auditor");
        
        AuditEvent[] memory events = new AuditEvent[](eventCounter.current());
        for (uint i = 0; i < eventCounter.current(); i++) {
            events[i] = auditTrail[i];
        }
        
        return events;
    }

    // Get Total Events
    function getTotalEvents() external view returns (uint256) {
        return eventCounter.current();
    }
}