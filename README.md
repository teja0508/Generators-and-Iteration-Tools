# EPAI3--Generators-and-Iteration-Tools
## Goal 1
Create a lazy iterator that will return a named tuple of the data in each row. The data types should be appropriate - i.e. if the column is a date, you should be storing dates in the named tuple, if the field is an integer, then it should be stored as an integer, etc.

## Goal 2
Calculate the number of violations by car make.

**Note**:
- Try to use lazy evaluation as much as possible - it may not always be possible though! That's OK, as long as it's kept to a minimum.
- No Test Cases
- Submit pending assignments

## Assignment Output

runfile('C:/Users/akayal/OneDrive - CSG Systems Inc/Deep Learning/EPAI-3/Session-13/Assignment/EPAI3--Generators-and-Iteration-Tools/epai_3_13_file_iterator.py', wdir='C:/Users/akayal/OneDrive - CSG Systems Inc/Deep Learning/EPAI-3/Session-13/Assignment/EPAI3--Generators-and-Iteration-Tools')
Reloaded modules: epai_3_13_lazy_iterator_generator, epai_3_13_lazy_iterator_file_reader

### Goal 1

- Use encryption keys to protect data when it is at rest within S3. We can use AWS encrypted API endpoint for data transfer. Data at rest can be 

```python

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
4006462396,22834JK,NY,COM,9/30/2016,5,VAN,CHEVR,BUS LANE VIOLATION

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
4007117810,21791MG,NY,COM,4/10/2017,5,VAN,DODGE,BUS LANE VIOLATION

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
4006265037,FZX9232,NY,PAS,8/23/2016,5,SUBN,FORD,BUS LANE VIOLATION

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
4006535600,N203399C,NY,OMT,10/19/2016,5,SUBN,FORD,BUS LANE VIOLATION

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
4007156700,92163MG,NY,COM,4/13/2017,5,VAN,FRUEH,BUS LANE VIOLATION

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
4006687989,MIQ600,SC,PAS,11/21/2016,5,VN,HONDA,BUS LANE VIOLATION

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
4006943052,2AE3984,MD,PAS,2/1/2017,5,SW,LINCO,BUS LANE VIOLATION

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
4007306795,HLG4926,NY,PAS,5/30/2017,5,SUBN,TOYOT,BUS LANE VIOLATION

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
4007124590,T715907C,NY,OMT,4/3/2017,5,SUBN,TOYOT,BUS LANE VIOLATION

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5096061966,HRC9475,NY,PAS,4/18/2017,7,SUBN,CADIL,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5094070400,DYP8042,NY,PAS,10/26/2016,7,SUBN,CHEVR,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5094906770,G30ESY,NJ,PAS,1/1/2017,7,WAGO,CHRYS,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5093319363,GGT8868,NY,PAS,9/6/2016,7,SUBN,CHRYS,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5092638849,107DDD,NY,SPO,7/20/2016,7,SUBN,DODGE,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5093455337,ENQT55,FL,PAS,9/12/2016,7,VN,DODGE,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5094961366,GSU4156,OH,PAS,1/7/2017,7,4S,DODGE,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5092906534,V84FXV,NJ,PAS,8/7/2016,7,WAGO,FIR,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5093620865,AD80228,AZ,PAS,9/24/2016,7,TK,FORD,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5092733548,EVX4041,NY,PAS,7/26/2016,7,SUBN,FORD,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5095995530,EMK5934,NY,PAS,4/13/2017,7,VAN,GMC,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5092750364,DPH8955,NY,PAS,7/27/2016,7,SUBN,HONDA,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5094658001,GCF1897,NY,PAS,12/10/2016,7,4DSD,HONDA,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5092833786,HCS9434,NY,PAS,8/3/2016,7,SUBN,HONDA,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5096484040,HHS1641,NY,PAS,5/17/2017,7,SUBN,HONDA,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5095797586,KHE1889,PA,PAS,3/28/2017,7,SDN,HONDA,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5095799807,VES2440,VA,PAS,3/29/2017,7,VAN,HONDA,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5093533919,CYU4598,NY,PAS,9/16/2016,7,SUBN,HYUND,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5093399735,DZGT24,FL,PAS,9/4/2016,7,UT,HYUND,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5094058873,GRN3101,NY,PAS,10/29/2016,7,4DSD,HYUND,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5094770986,T668962C,NY,OMT,12/19/2016,7,4DSD,HYUND,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5093895611,GVZ1407,NY,PAS,10/14/2016,7,4DSD,JAGUA,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5094185792,AGM9013,NY,PAS,11/4/2016,7,SUBN,JEEP,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5092708219,F47DZF,NJ,PAS,7/24/2016,7,4 DR,JEEP,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5094759954,GLB8157,NY,PAS,12/19/2016,7,SUBN,JEEP,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5093891046,FJS4033,NY,PAS,10/14/2016,7,4DSD,LEXUS,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5093527853,GYM9809,NY,PAS,9/21/2016,7,4DSD,LEXUS,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5096683886,HCS4873,NY,PAS,5/18/2017,7,4DSD,LEXUS,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5096917368,FZD8593,NY,PAS,6/13/2017,7,SUBN,ME/BE,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5094893737,GER1584,NY,PAS,12/31/2016,7,4DSD,ME/BE,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5096249300,HEM8411,NY,PAS,5/1/2017,7,4DSD,ME/BE,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5096958772,165TRX,CT,PAS,6/16/2017,7,4W,MERCU,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5093703217,HFG4313,NY,PAS,9/30/2016,7,4DSD,MITSU,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5094670736,AXU4790,NY,PAS,12/11/2016,7,4DSD,NISSA,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5094094166,CZM4111,NY,PAS,10/28/2016,7,4DSD,TOYOT,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5096723768,EDN2797,NY,PAS,6/2/2017,7,4DSD,TOYOT,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5093209120,FZT5005,NY,PAS,8/28/2016,7,4DSD,TOYOT,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5092469481,GZH7067,NY,PAS,7/10/2016,7,SUBN,TOYOT,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5092451658,GZH7067,NY,PAS,7/8/2016,7,SUBN,TOYOT,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
5095356545,GZM8254,NY,OMS,2/18/2017,7,SUBN,TOYOT,FAILURE TO STOP AT RED LIGHT

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8410006650,D53AUUN,NJ,PAS,10/21/2016,9,4DSD,LEXUS,09-Blocking the Box

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8534116519,CES6482,NY,PAS,6/12/2017,9,SUBN,TOYOT,09-Blocking the Box

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8485674984,T713160C,NY,OMT,6/13/2017,9,SUBN,TOYOT,09-Blocking the Box

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8556557405,59622JW,NY,COM,6/9/2017,10,VAN,FORD,10-No Stopping

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8071038416,AM479F,NJ,PAS,7/7/2016,10,DELV,FRUEH,10-No Stopping

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8483087236,76822MH,NY,COM,5/19/2017,10,DELV,HIN,10-No Stopping

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8481125088,55179ME,NY,COM,4/10/2017,10,DELV,NS/OT,10-No Stopping

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8506822300,55106MB,NY,COM,5/31/2017,10,VAN,WORKH,10-No Stopping

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8482331425,86609MB,NY,COM,6/18/2017,13,VAN,CHEVR,13-No Stand (taxi stand)

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8028246722,T703619C,NY,OMT,9/15/2016,13,SUBN,CHEVR,13-No Stand (taxi stand)

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8378547530,FWZ8815,NY,PAS,1/11/2017,14,2DSD,ACURA,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8489750210,6DQT356,CA,PAS,11/28/2016,14,4DSD,AUDI,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
1410726095,DEP4792,NC,PAS,7/15/2016,14,,BMW,

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8421031235,GGA4266,NY,PAS,10/18/2016,14,4DSD,BMW,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
7730553259,DLZ8901,NY,PAS,9/26/2016,14,SUBN,CHEVR,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8498520046,HKF6916,NY,PAS,4/27/2017,14,SUBN,CHEVR,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8537807813,HNF6718,NY,PAS,4/21/2017,14,SUBN,CHEVR,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8083571465,KCG9559,PA,PAS,12/22/2016,14,SUBN,CHEVR,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
7536689184,ZCL5723,PA,PAS,1/26/2017,14,VAN,CHEVR,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8480505680,HCT2134,NY,PAS,1/18/2017,14,SUBN,CHRYS,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8481973580,28693MH,NY,COM,6/13/2017,14,VAN,DODGE,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8460500214,30408MC,NY,COM,8/4/2016,14,PICK,DODGE,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8482817036,50501JT,NY,COM,4/11/2017,14,VAN,DODGE,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8117027999,83317ME,NY,COM,9/27/2016,14,VAN,DODGE,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8488121532,FLX2674,NY,PAS,4/5/2017,14,2DSD,DODGE,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8543952980,FSZ8671,NY,PAS,4/21/2017,14,SUBN,DODGE,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8501806912,KGP1166,PA,PAS,6/4/2017,14,VAN,DODGE,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8107542976,11AH74,MA,PAS,1/29/2017,14,4DSD,FORD,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8564650320,29222MK,NY,COM,5/5/2017,14,VAN,FORD,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8010367576,30661MA,NY,COM,12/22/2016,14,VAN,FORD,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8505159536,41795JX,NY,COM,3/9/2017,14,VAN,FORD,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
7813887440,44267JZ,NY,COM,8/12/2016,14,VAN,FORD,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8440509546,49317JX,NY,COM,10/29/2016,14,VAN,FORD,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
1408575656,6XWZ969,CA,PAS,7/6/2016,14,SDN,FORD,

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8516853275,72100MH,NY,COM,4/12/2017,14,VAN,FORD,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
7059924103,91878MB,NY,COM,10/12/2016,14,VAN,FORD,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8170085561,ENM3708,NY,PAS,2/10/2017,14,SUBN,FORD,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8527511113,F70GEP,NJ,PAS,5/1/2017,14,SUBN,FORD,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8511453696,FSY6987,NY,PAS,3/13/2017,14,SUBN,FORD,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
1413745933,HCC2829,NY,PAS,8/22/2016,14,VAN,FORD,

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8484882226,S25DSK,NJ,PAS,6/8/2017,14,PICK,FORD,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8524054499,ZRK24R,NJ,PAS,3/18/2017,14,SUBN,FORD,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
1423945281,2240653,IN,PAS,5/13/2017,14,,FRUEH,

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8577650820,10632JU,NY,COM,6/20/2017,14,UTIL,FRUEH,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
7056662882,83038ME,NY,COM,9/21/2016,14,VAN,FRUEH,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8324025510,83146ME,NY,COM,10/27/2016,14,VAN,FRUEH,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8286541110,85846MD,NY,COM,10/25/2016,14,VAN,FRUEH,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8270548250,91028MJ,NY,COM,12/13/2016,14,DELV,FRUEH,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
8480520395,99886MC,NY,COM,6/19/2017,14,VAN,FRUEH,14-No Standing

parking_details(summonsNumber='SummonsNumber', plateID='PlateID', registrationState='RegistrationState', plateType='PlateType', issueDate='IssueDate', violationCode='ViolationCode', vehicleBodyType='VehicleBodyType', vehicleMake='VehicleMake', violationDescription='ViolationDescription')
```
### Goal 2

```python
Number of Violation by Car Make:Vehicle Make
TOYOT    100
FORD      98
HONDA     94
CHEVR     66
NISSA     59
DODGE     43
FRUEH     38
ME/BE     36
GMC       33
HYUND     32
BMW       32
LEXUS     25
INTER     23
JEEP      21
NS/OT     18
SUBAR     17
INFIN     13
AUDI      12
ACURA     12
VOLVO     11
LINCO     11
CHRYS     11
ISUZU      9
CADIL      9
MITSU      8
KIA        7
VOLKS      7
HIN        6
ROVER      5
KENWO      5
MAZDA      5
MERCU      4
BUICK      4
JAGUA      3
PORSC      3
SMART      3
SCION      2
HINO       2
WORKH      2
SAAB       2
STAR       1
SPRI       1
SATUR      1
UD         1
UPS        1
BSA        1
PETER      1
PONTI      1
PLYMO      1
OLDSM      1
CITRO      1
MINI       1
MI/F       1
AM/T       1
FIR        1
GEO        1
YAMAH      1
FIAT       0
UTILI      0
GMCQ       0
Name: Violation Description, dtype: int64
```

