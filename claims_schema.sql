CREATE TABLE Patients (
    PatientID INT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT,
    Gender VARCHAR(10),
    Region VARCHAR(50)
);

CREATE TABLE Providers (
    ProviderID INT PRIMARY KEY,
    Name VARCHAR(100),
    Specialty VARCHAR(50)
);

CREATE TABLE Diagnoses (
    DiagnosisID INT PRIMARY KEY,
    Code VARCHAR(10),
    Description TEXT
);

CREATE TABLE Claims (
    ClaimID INT PRIMARY KEY,
    PatientID INT,
    ProviderID INT,
    DiagnosisID INT,
    ClaimAmount DECIMAL(10,2),
    ClaimDate DATE,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (ProviderID) REFERENCES Providers(ProviderID),
    FOREIGN KEY (DiagnosisID) REFERENCES Diagnoses(DiagnosisID)
);
