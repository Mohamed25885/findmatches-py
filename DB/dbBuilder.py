import dbAccessLayer

sqlCreateTable = '''
Create Table IF NOT EXISTS scores (
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    level INTEGER DEFAULT 1,
    time DECIMAL NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT unique_name_level unique(name, level),
    PRIMARY KEY (id)
)
'''
#dbAccessLayer.buildQuery(sqlCreateTable)

#dbAccessLayer.dropTable("scores")

#dbAccessLayer.insertIntoScore("ahmed", 104, 3)

print(dbAccessLayer.getLevel(3)[0])