
from sqlalchemy import Column,Integer,String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#1. Define the base class
Base = declarative_base()
print("Base class is intialized..!")
#2. defined the model 
class Department(Base):
	__tablename__ ='depts'
	deptno = Column(String(10),primary_key=True)
	name = Column(String(30))
	loc = Column(String(20))
	
        
print("Model class is declared..!")
	
#3. Create a Engine
#engine = create_engine("mysql+pymysql://root:Password'\@'1@localhost/training", echo=True)

engine = create_engine("sqlite:///training.db", echo=True)



# 4. create tables
Base.metadata.create_all(engine)

print("Tables are created in the database")

#. create a session

Session = sessionmaker(bind=engine)
session = Session()
print("Session is creted...!")

#dept1 = Department(deptno='50',name='Microbio',loc='Chicago')
#dept2= Department(deptno='60',name='Genetics',loc='NewYork')
#dept3 = Department(deptno='70',name='Statistics',loc='Dallas')
#dept4 = Department(deptno='80',name='Anthropology',loc='LosAngeles')

#session.add_all([dept1,dept2,dept3,dept4])
#session.commit()
#print("Records inserted...!")

#To select all rows 
#depts = session.query(Department).all()
#for dept in depts:
#	print(f"{dept.deptno} - {dept.name} - {dept.loc}")


# to seletc the rows based on condition
depts = session.query(Department).filter(Department.loc == 'Chicago').all()
for dept in depts:
	print(f"{dept.deptno} - {dept.name} - {dept.loc}")
	

#to delete a particular record
#dept = session.query(Department).filter_by(deptno='10').first()
#session.delete(dept)
#session.commit()
#print("Record deleted with id 10")

depts = session.query(Department).filter(Department.loc == 'Chicago').all()
for dept in depts:
	print(f"{dept.deptno} - {dept.name} - {dept.loc}")


#update operation
dept = session.query(Department).filter_by(name='Microbio').first()
dept.name = "Microbiology"
session.commit()
print("The record udpated..!")
	
depts = session.query(Department).all()
for dept in depts:
	print(f"{dept.deptno} - {dept.name} - {dept.loc}")
