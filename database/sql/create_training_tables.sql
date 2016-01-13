DROP TABLE IF EXISTS Training-Littera_Notabilior;
CREATE TABLE Training-Littera_Notabilior (
	ID INT NOT NULL AUTO_INCREMENT,
	MS_Number VARCHAR(4) NOT NULL,
	F_Number VARCHAR(8) NOT NULL,
	X INT(4) NOT NULL,
	Y INT(4) NOT NULL,
	Width INT(4),
	Height INT(4),
	Primary_Color VARCHAR(16),
	Letter CHAR(1),
	IsError TINYINT(1),

	PRIMARY KEY (ID),
	UNIQUE (MS_Number, F_Number, X, Y),
	FOREIGN KEY (F_Number, MS_Number) REFERENCES Folio(Number, MS_Number)
);

DROP TABLE IF EXISTS LN_Second_Colors;
CREATE TABLE LN_Second_Colors (
	LN_ID INT,
	Color VARCHAR(16),
	PRIMARY KEY (LN_ID, Color),
	FOREIGN KEY (LN_ID) REFERENCES Training-Littera_Notabilior(ID)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);


DROP TABLE IF EXISTS Training-Enlarged_Capital;
CREATE TABLE Training-Enlarged_Capital (
	ID int AUTO_INCREMENT,
	MS_Number VARCHAR(4) NOT NULL,
	F_Number VARCHAR(8) NOT NULL,
	X INT(4) NOT NULL,
	Y INT(4) NOT NULL,
	Width INT(4),
	Height INT(4),
	Primary_Color VARCHAR(16),
	Letter CHAR(1),
	IsError TINYINT(1),

	PRIMARY KEY (ID),
	UNIQUE (MS_Number, F_Number, X, Y),
	FOREIGN KEY (F_Number, MS_Number) REFERENCES Folio(Number, RV, MS_Number)
);

DROP TABLE IF EXISTS EC_Second_Colors;
CREATE TABLE EC_Second_Colors (
	EC_ID INT,
	Color VARCHAR(16),
	PRIMARY KEY (EC_ID, Color),
	FOREIGN KEY (EC_ID) REFERENCES Training-Enlarged_Capital(ID)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Training-Rubric;
CREATE TABLE Training-Rubric (
	ID int AUTO_INCREMENT,
	MS_Number VARCHAR(4) NOT NULL, 
	F_Number VARCHAR(8) NOT NULL,
	X INT(4) NOT NULL,
	Y INT(4) NOT NULL,
	Width INT(4),
	Height INT(4),
	IsError TINYINT(1),

	PRIMARY KEY (ID),
	UNIQUE (MS_Number, F_Number, X, Y),
	FOREIGN KEY (F_Number, MS_Number) REFERENCES Folio(Number, RV, MS_Number)
);

DROP TABLE IF EXISTS Training-Intertextual_Space;
CREATE TABLE Training-Intertextual_Space (
	ID int AUTO_INCREMENT,
	MS_Number VARCHAR(4) NOT NULL,
	F_Number VARCHAR(8) NOT NULL,
	X INT(4) NOT NULL,
	Y INT(4) NOT NULL,
	Width INT(4),
	Height INT(4),
	IsError TINYINT(1),

	PRIMARY KEY (ID),
	UNIQUE (MS_Number, F_Number, X, Y),
	FOREIGN KEY (F_Number, MS_Number) REFERENCES Folio(Number, RV, MS_Number)
);

