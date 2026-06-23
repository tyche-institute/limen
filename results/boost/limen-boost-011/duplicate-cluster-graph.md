# Duplicate-Cluster Graph

```mermaid
graph TD
    A[Case C-2023-001] -->|AIID-2023-045| B[MITRE ATLAS-1122]
    A -->|OECD-AIM-0089| C[OECD AI Principles]
    B --> D[Security Failure Pattern]
    C --> E[Governance Pattern]
    
    F[Case C-2023-002] -->|AIID-2023-078| G[MITRE ATLAS]
    F -->|ISO-IEC-42001-011| H[ISO Standalone]
    G --> I[Accountability Gap]
    H --> J[Compliance Framework]
    
    K[Cluster 001] --> A
    K --> F
    
    style A fill:#FFDAB9,stroke:#333
    style F fill:#FFDAB9,stroke:#333
    style K fill:#FF9966,stroke:#333
```

## Notes
- Cluster 001 groups both cases due to shared crosswalk framework (MITRE ATLAS)
- Visualizes how cases map to different frameworks and patterns
- Suggests further analysis of accountability gaps in public-sector AI systems