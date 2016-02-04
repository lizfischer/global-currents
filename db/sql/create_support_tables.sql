DROP TABLE IF EXISTS Manuscript;
CREATE TABLE Manuscript (
	Number VARCHAR(4),
	Title VARCHAR(64),
	Columns TINYINT(1),
	PRIMARY KEY(Number)
);

DROP TABLE IF EXISTS Date;
CREATE TABLE Date (
	Century TINYINT(2),
	Super VARCHAR(4),
	MS_Number VARCHAR(4),
	PRIMARY KEY (Century, Super, MS_Number),
	FOREIGN KEY (MS_Number) REFERENCES Manuscript(Number)
);

DROP TABLE IF EXISTS Language;
CREATE TABLE Language (
	Language VARCHAR(16),
	MS_Number VARCHAR(4),
	PRIMARY KEY (Language, MS_Number)
);

DROP TABLE IF EXISTS Location;
CREATE TABLE Location (
	Region VARCHAR(64),
	Institution VARCHAR(64),
	MS_Number VARCHAR(4),
	W INT(5),
	H INT(5),
	FOREIGN KEY (MS_Number) REFERENCES Manuscript(Number)
);

DROP TABLE IF EXISTS Folio;
CREATE TABLE Folio (
	Number VARCHAR(8),
	MS_Number VARCHAR(4),
	URL VARCHAR(128),
	PRIMARY KEY (Number, MS_Number),
	FOREIGN KEY (MS_Number) REFERENCES Manuscript(Number)	
);
