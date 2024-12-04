contract ContractAudit is AccessControl, Pausable, ReentrancyGuard {
    bytes32 public constant ADMIN_ROLE = keccak256("ADMIN_ROLE");

    enum ActionType { 
        VIEW, 
        UPDATE, 
        ACCESS_GRANTED, 
        ACCESS_REVOKED,
        EMERGENCY_ACCESS 
    }

    struct AuditLog {
        address actor;
        address patient;
        ActionType actionType;
        uint256 timestamp;
        string details;
    }

    AuditLog[] private auditLogs;

    event AuditLogCreated(
        address indexed actor, 
        address indexed patient, 
        ActionType actionType, 
        uint256 timestamp
    );

    constructor() {
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(ADMIN_ROLE, msg.sender);
    }

    /**
     * @dev Log an audit entry
     */
    function logAction(
        address patient, 
        ActionType actionType, 
        string memory details
    ) external {
        AuditLog memory newLog = AuditLog({
            actor: msg.sender,
            patient: patient,
            actionType: actionType,
            timestamp: block.timestamp,
            details: details
        });

        auditLogs.push(newLog);
        emit AuditLogCreated(msg.sender, patient, actionType, block.timestamp);
    }

    /**
     * @dev Retrieve audit logs for a specific patient
     */
    function getPatientAuditLogs(address patient) external view returns (AuditLog[] memory) {
        uint256 count = 0;
        for (uint256 i = 0; i < auditLogs.length; i++) {
            if (auditLogs[i].patient == patient) {
                count++;
            }
        }

        AuditLog[] memory patientLogs = new AuditLog[](count);
        uint256 index = 0;
        for (uint256 i = 0; i < auditLogs.length; i++) {
            if (auditLogs[i].patient == patient) {
                patientLogs[index] = auditLogs[i];
                index++;
            }
        }

        return patientLogs;
    }

    function pause() external onlyRole(ADMIN_ROLE) {
        _pause();
    }

    function unpause() external onlyRole(ADMIN_ROLE) {
        _unpause();
    }
}