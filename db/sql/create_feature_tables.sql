DROP TABLE IF EXISTS littera_notabilior;
CREATE TABLE littera_notabilior (
	url VARCHAR(128) NOT NULL,
	letter CHAR(1),
	primaryColor VARCHAR(16),
	msNumber VARCHAR(4) NOT NULL,
	folioNumber VARCHAR(8) NOT NULL,
	x INT(4) NOT NULL,
	y INT(4) NOT NULL,
	w INT(4),
	h INT(4),
	isError TINYINT(1),
    errorType CHAR(2),

	PRIMARY KEY (url),
	UNIQUE (msNumber, folioNumber, x, y),
	FOREIGN KEY (folioNumber, msNumber) REFERENCES folio(number, msNumber)
);

DROP TABLE IF EXISTS lnSecondColors;
CREATE TABLE lnSecondColors (
	url VARCHAR(128) NOT NULL,
	color VARCHAR(16) NOT NULL,
	PRIMARY KEY (url, color),
	FOREIGN KEY (url) REFERENCES littera_notabilior(url)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);

DROP TABLE IF EXISTS enlarged_capital;
CREATE TABLE enlarged_capital (
	url int AUTO_INCREMENT,
	msNumber VARCHAR(4) NOT NULL,
	folioNumber VARCHAR(8) NOT NULL,
	x INT(4) NOT NULL,
	y INT(4) NOT NULL,
	w INT(4),
	h INT(4),
	primaryColor VARCHAR(16),
	letter CHAR(1),
	isError TINYINT(1),

	PRIMARY KEY (url),
	UNIQUE (MS_Number, folioNumber, X, Y),
	FOREIGN KEY (F_Number, MS_Number) REFERENCES Folio(Number, RV, MS_Number)
);


DROP TABLE IF EXISTS ecSecondColors;
CREATE TABLE ecSecondColors (
	url INT,
	color VARCHAR(16),
	PRIMARY KEY (url, color),
	FOREIGN KEY (url) REFERENCES enlarged_capital(url)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);

DROP TABLE IF EXISTS Rubric;
CREATE TABLE Rubric (
	ID int AUTO_INCREMENT,
	MS_Number VARCHAR(4) NOT NULL, 
	F_Number VARCHAR(8) NOT NULL,
	X INT(4) NOT NULL,
	Y INT(4) NOT NULL,
	Width INT(4),
	Height INT(4),
	IsError TINYINT(1),

	PRIMARY KEY (ID),
	UNIQUE (MS_Number, F_Number, x, Y),
	FOREIGN KEY (F_Number, MS_Number) REFERENCES Folio(Number, RV, MS_Number)
);

DROP TABLE IF EXISTS Intertextual_Space;
CREATE TABLE Intertextual_Space (
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
