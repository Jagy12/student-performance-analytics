INSERT INTO Departments
VALUES
('DEP001','Biological Sciences'),
('DEP002','Physical Sciences'),
('DEP003','Mathematical & Computational Sciences'),
('DEP004','Humanities'),
('DEP005','Social Sciences'),
('DEP006','Arts & Design'),
('DEP007','Business Administration'),
('DEP008','Finance'),
('DEP009','Engineering & Technology'),
('DEP010','Health & Professional Programs');


INSERT INTO Students
VALUES
('STU001','Aarav Sharma','9876500001','Mumbai','DEP001','Biology'),
('STU002','Aanya Patel','9876500002','Pune','DEP001','Botany'),
('STU003','Abhinav Singh','9876500003','Delhi','DEP001','Zoology'),
('STU004','Ananya Verma','9876500004','Bangalore','DEP001','Biology'),
('STU005','Arjun Mehta','9876500005','Hyderabad','DEP001','Botany'),

('STU006','Bhavesh Gupta','9876500006','Chennai','DEP002','Physics'),
('STU007','Bhavya Nair','9876500007','Kochi','DEP002','Chemistry'),
('STU008','Brijesh Kumar','9876500008','Jaipur','DEP002','Earth Science'),
('STU009','Bhoomi Shah','9876500009','Ahmedabad','DEP002','Physics'),
('STU010','Bharat Jain','9876500010','Indore','DEP002','Chemistry'),

('STU011','Charvi Kapoor','9876500011','Delhi','DEP003','Mathematics'),
('STU012','Chetan Yadav','9876500012','Lucknow','DEP003','Statistics'),
('STU013','Chirag Malhotra','9876500013','Noida','DEP003','Computer Science'),
('STU014','Chhavi Sharma','9876500014','Chandigarh','DEP003','Mathematics'),
('STU015','Cyrus Dsouza','9876500015','Goa','DEP003','Statistics'),

('STU016','Deepak Mishra','9876500016','Patna','DEP004','English Literature'),
('STU017','Divya Menon','9876500017','Kochi','DEP004','History'),
('STU018','Daksh Gupta','9876500018','Kanpur','DEP004','Philosophy'),
('STU019','Diya Kapoor','9876500019','Delhi','DEP004','History'),
('STU020','Darsh Patel','9876500020','Surat','DEP004','English Literature'),
('STU021','Esha Roy','9876500021','Kolkata','DEP005','Psychology'),
('STU022','Ethan Das','9876500022','Kolkata','DEP005','Sociology'),
('STU023','Ekta Sharma','9876500023','Jaipur','DEP005','Economics'),
('STU024','Eshaan Gupta','9876500024','Delhi','DEP005','Psychology'),
('STU025','Elina Thomas','9876500025','Kochi','DEP005','Sociology'),

('STU026','Farhan Khan','9876500026','Mumbai','DEP006','Fine Arts'),
('STU027','Falguni Shah','9876500027','Ahmedabad','DEP006','Music'),
('STU028','Faizan Ali','9876500028','Lucknow','DEP006','Graphic Design'),
('STU029','Fiona Dsouza','9876500029','Goa','DEP006','Fine Arts'),
('STU030','Firoz Sheikh','9876500030','Pune','DEP006','Music'),

('STU031','Gauri Joshi','9876500031','Nagpur','DEP007','Management'),
('STU032','Gautam Mehta','9876500032','Surat','DEP007','Marketing'),
('STU033','Geet Kapoor','9876500033','Delhi','DEP007','Entrepreneurship'),
('STU034','Girish Nair','9876500034','Kochi','DEP007','Management'),
('STU035','Gunjan Verma','9876500035','Bhopal','DEP007','Marketing'),

('STU036','Harsh Jain','9876500036','Indore','DEP008','Accounting'),
('STU037','Hina Patel','9876500037','Ahmedabad','DEP008','Banking'),
('STU038','Hitesh Kumar','9876500038','Patna','DEP008','Corporate Finance'),
('STU039','Heena Shah','9876500039','Surat','DEP008','Accounting'),
('STU040','Hriday Singh','9876500040','Delhi','DEP008','Banking'),

('STU041','Ishaan Rao','9876500041','Bangalore','DEP009','Programming Fundamentals'),
('STU042','Ira Menon','9876500042','Chennai','DEP009','DBMS'),
('STU043','Imran Khan','9876500043','Hyderabad','DEP009','Data Structures'),
('STU044','Ishita Sharma','9876500044','Pune','DEP009','Programming Fundamentals'),
('STU045','Ivan Dsouza','9876500045','Goa','DEP009','DBMS'),

('STU046','Jiya Patel','9876500046','Mumbai','DEP010','Nursing'),
('STU047','Jatin Gupta','9876500047','Delhi','DEP010','Public Health'),
('STU048','Juhi Kapoor','9876500048','Chandigarh','DEP010','Medical Sciences'),
('STU049','Jay Mehta','9876500049','Ahmedabad','DEP010','Nursing'),
('STU050','Janvi Shah','9876500050','Surat','DEP010','Public Health');


INSERT INTO Subjects
VALUES
('SUB001','Biology','DEP001'),
('SUB002','Botany','DEP001'),
('SUB003','Zoology','DEP001'),

('SUB004','Physics','DEP002'),
('SUB005','Chemistry','DEP002'),
('SUB006','Earth Science','DEP002'),

('SUB007','Mathematics','DEP003'),
('SUB008','Statistics','DEP003'),
('SUB009','Computer Science','DEP003'),

('SUB010','English Literature','DEP004'),
('SUB011','History','DEP004'),
('SUB012','Philosophy','DEP004'),

('SUB013','Psychology','DEP005'),
('SUB014','Sociology','DEP005'),
('SUB015','Economics','DEP005'),

('SUB016','Fine Arts','DEP006'),
('SUB017','Music','DEP006'),
('SUB018','Graphic Design','DEP006'),

('SUB019','Management','DEP007'),
('SUB020','Marketing','DEP007'),
('SUB021','Entrepreneurship','DEP007'),

('SUB022','Accounting','DEP008'),
('SUB023','Banking','DEP008'),
('SUB024','Corporate Finance','DEP008'),

('SUB025','Programming Fundamentals','DEP009'),
('SUB026','DBMS','DEP009'),
('SUB027','Data Structures','DEP009'),

('SUB028','Nursing','DEP010'),
('SUB029','Public Health','DEP010'),
('SUB030','Medical Sciences','DEP010');

INSERT INTO Student_Subjects VALUES

-- DEP001
('STU001','SUB001'),('STU001','SUB002'),('STU001','SUB003'),
('STU002','SUB001'),('STU002','SUB002'),('STU002','SUB003'),
('STU003','SUB001'),('STU003','SUB002'),('STU003','SUB003'),
('STU004','SUB001'),('STU004','SUB002'),('STU004','SUB003'),
('STU005','SUB001'),('STU005','SUB002'),('STU005','SUB003'),

-- DEP002
('STU006','SUB004'),('STU006','SUB005'),('STU006','SUB006'),
('STU007','SUB004'),('STU007','SUB005'),('STU007','SUB006'),
('STU008','SUB004'),('STU008','SUB005'),('STU008','SUB006'),
('STU009','SUB004'),('STU009','SUB005'),('STU009','SUB006'),
('STU010','SUB004'),('STU010','SUB005'),('STU010','SUB006'),

-- DEP003
('STU011','SUB007'),('STU011','SUB008'),('STU011','SUB009'),
('STU012','SUB007'),('STU012','SUB008'),('STU012','SUB009'),
('STU013','SUB007'),('STU013','SUB008'),('STU013','SUB009'),
('STU014','SUB007'),('STU014','SUB008'),('STU014','SUB009'),
('STU015','SUB007'),('STU015','SUB008'),('STU015','SUB009'),

-- DEP004
('STU016','SUB010'),('STU016','SUB011'),('STU016','SUB012'),
('STU017','SUB010'),('STU017','SUB011'),('STU017','SUB012'),
('STU018','SUB010'),('STU018','SUB011'),('STU018','SUB012'),
('STU019','SUB010'),('STU019','SUB011'),('STU019','SUB012'),
('STU020','SUB010'),('STU020','SUB011'),('STU020','SUB012'),

-- DEP005
('STU021','SUB013'),('STU021','SUB014'),('STU021','SUB015'),
('STU022','SUB013'),('STU022','SUB014'),('STU022','SUB015'),
('STU023','SUB013'),('STU023','SUB014'),('STU023','SUB015'),
('STU024','SUB013'),('STU024','SUB014'),('STU024','SUB015'),
('STU025','SUB013'),('STU025','SUB014'),('STU025','SUB015'),

-- DEP006
('STU026','SUB016'),('STU026','SUB017'),('STU026','SUB018'),
('STU027','SUB016'),('STU027','SUB017'),('STU027','SUB018'),
('STU028','SUB016'),('STU028','SUB017'),('STU028','SUB018'),
('STU029','SUB016'),('STU029','SUB017'),('STU029','SUB018'),
('STU030','SUB016'),('STU030','SUB017'),('STU030','SUB018'),

-- DEP007
('STU031','SUB019'),('STU031','SUB020'),('STU031','SUB021'),
('STU032','SUB019'),('STU032','SUB020'),('STU032','SUB021'),
('STU033','SUB019'),('STU033','SUB020'),('STU033','SUB021'),
('STU034','SUB019'),('STU034','SUB020'),('STU034','SUB021'),
('STU035','SUB019'),('STU035','SUB020'),('STU035','SUB021'),

-- DEP008
('STU036','SUB022'),('STU036','SUB023'),('STU036','SUB024'),
('STU037','SUB022'),('STU037','SUB023'),('STU037','SUB024'),
('STU038','SUB022'),('STU038','SUB023'),('STU038','SUB024'),
('STU039','SUB022'),('STU039','SUB023'),('STU039','SUB024'),
('STU040','SUB022'),('STU040','SUB023'),('STU040','SUB024'),

-- DEP009
('STU041','SUB025'),('STU041','SUB026'),('STU041','SUB027'),
('STU042','SUB025'),('STU042','SUB026'),('STU042','SUB027'),
('STU043','SUB025'),('STU043','SUB026'),('STU043','SUB027'),
('STU044','SUB025'),('STU044','SUB026'),('STU044','SUB027'),
('STU045','SUB025'),('STU045','SUB026'),('STU045','SUB027'),

-- DEP010
('STU046','SUB028'),('STU046','SUB029'),('STU046','SUB030'),
('STU047','SUB028'),('STU047','SUB029'),('STU047','SUB030'),
('STU048','SUB028'),('STU048','SUB029'),('STU048','SUB030'),
('STU049','SUB028'),('STU049','SUB029'),('STU049','SUB030'),
('STU050','SUB028'),('STU050','SUB029'),('STU050','SUB030');


INSERT INTO Marks (student_id,subject_id,marks)
VALUES

-- STU001-STU005 (Biological Sciences)
('STU001','SUB001',88),('STU001','SUB002',91),('STU001','SUB003',85),
('STU002','SUB001',76),('STU002','SUB002',81),('STU002','SUB003',79),
('STU003','SUB001',93),('STU003','SUB002',95),('STU003','SUB003',90),
('STU004','SUB001',72),('STU004','SUB002',78),('STU004','SUB003',80),
('STU005','SUB001',84),('STU005','SUB002',87),('STU005','SUB003',82),

-- STU006-STU010 (Physical Sciences)
('STU006','SUB004',89),('STU006','SUB005',92),('STU006','SUB006',86),
('STU007','SUB004',68),('STU007','SUB005',72),('STU007','SUB006',70),
('STU008','SUB004',94),('STU008','SUB005',97),('STU008','SUB006',91),
('STU009','SUB004',61),('STU009','SUB005',65),('STU009','SUB006',63),
('STU010','SUB004',78),('STU010','SUB005',82),('STU010','SUB006',80),

-- STU011-STU015 (Mathematics & CS)
('STU011','SUB007',96),('STU011','SUB008',94),('STU011','SUB009',98),
('STU012','SUB007',73),('STU012','SUB008',76),('STU012','SUB009',71),
('STU013','SUB007',91),('STU013','SUB008',89),('STU013','SUB009',95),
('STU014','SUB007',66),('STU014','SUB008',69),('STU014','SUB009',64),
('STU015','SUB007',58),('STU015','SUB008',62),('STU015','SUB009',60),

-- STU016-STU020 (Humanities)
('STU016','SUB010',82),('STU016','SUB011',79),('STU016','SUB012',85),
('STU017','SUB010',88),('STU017','SUB011',91),('STU017','SUB012',86),
('STU018','SUB010',55),('STU018','SUB011',59),('STU018','SUB012',57),
('STU019','SUB010',74),('STU019','SUB011',77),('STU019','SUB012',73),
('STU020','SUB010',92),('STU020','SUB011',95),('STU020','SUB012',90),

-- STU021-STU025 (Social Sciences)
('STU021','SUB013',81),('STU021','SUB014',84),('STU021','SUB015',79),
('STU022','SUB013',67),('STU022','SUB014',70),('STU022','SUB015',65),
('STU023','SUB013',90),('STU023','SUB014',93),('STU023','SUB015',88),
('STU024','SUB013',53),('STU024','SUB014',56),('STU024','SUB015',51),
('STU025','SUB013',77),('STU025','SUB014',80),('STU025','SUB015',75),

-- STU026-STU030 (Arts & Design)
('STU026','SUB016',95),('STU026','SUB017',97),('STU026','SUB018',94),
('STU027','SUB016',72),('STU027','SUB017',75),('STU027','SUB018',71),
('STU028','SUB016',63),('STU028','SUB017',66),('STU028','SUB018',60),
('STU029','SUB016',86),('STU029','SUB017',89),('STU029','SUB018',85),
('STU030','SUB016',49),('STU030','SUB017',52),('STU030','SUB018',47),

-- STU031-STU035 (Business)
('STU031','SUB019',91),('STU031','SUB020',94),('STU031','SUB021',89),
('STU032','SUB019',74),('STU032','SUB020',78),('STU032','SUB021',73),
('STU033','SUB019',83),('STU033','SUB020',86),('STU033','SUB021',81),
('STU034','SUB019',58),('STU034','SUB020',61),('STU034','SUB021',56),
('STU035','SUB019',69),('STU035','SUB020',72),('STU035','SUB021',68),

-- STU036-STU040 (Finance)
('STU036','SUB022',97),('STU036','SUB023',95),('STU036','SUB024',98),
('STU037','SUB022',82),('STU037','SUB023',85),('STU037','SUB024',80),
('STU038','SUB022',64),('STU038','SUB023',68),('STU038','SUB024',62),
('STU039','SUB022',55),('STU039','SUB023',58),('STU039','SUB024',53),
('STU040','SUB022',88),('STU040','SUB023',91),('STU040','SUB024',87),

-- STU041-STU045 (Engineering & Technology)
('STU041','SUB025',94),('STU041','SUB026',96),('STU041','SUB027',93),
('STU042','SUB025',78),('STU042','SUB026',81),('STU042','SUB027',76),
('STU043','SUB025',85),('STU043','SUB026',88),('STU043','SUB027',84),
('STU044','SUB025',62),('STU044','SUB026',65),('STU044','SUB027',60),
('STU045','SUB025',51),('STU045','SUB026',55),('STU045','SUB027',49),

-- STU046-STU050 (Health & Professional Programs)
('STU046','SUB028',89),('STU046','SUB029',92),('STU046','SUB030',87),
('STU047','SUB028',76),('STU047','SUB029',79),('STU047','SUB030',74),
('STU048','SUB028',95),('STU048','SUB029',97),('STU048','SUB030',94),
('STU049','SUB028',68),('STU049','SUB029',71),('STU049','SUB030',66),
('STU050','SUB028',57),('STU050','SUB029',60),('STU050','SUB030',55);

INSERT INTO Attendance (student_id,attendance_percentage)
VALUES
('STU001',96),('STU002',88),('STU003',98),('STU004',84),('STU005',93),
('STU006',91),('STU007',87),('STU008',95),('STU009',82),('STU010',89),
('STU011',99),('STU012',85),('STU013',97),('STU014',81),('STU015',78),
('STU016',92),('STU017',94),('STU018',73),('STU019',86),('STU020',98),
('STU021',90),('STU022',83),('STU023',96),('STU024',71),('STU025',88),
('STU026',99),('STU027',84),('STU028',79),('STU029',92),('STU030',68),
('STU031',95),('STU032',87),('STU033',91),('STU034',74),('STU035',82),
('STU036',99),('STU037',89),('STU038',77),('STU039',72),('STU040',93),
('STU041',97),('STU042',85),('STU043',90),('STU044',76),('STU045',69),
('STU046',94),('STU047',86),('STU048',99),('STU049',81),('STU050',73);
