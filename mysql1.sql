# create table `student1`
# (`student1_id` int primary key auto_increment,
# `name` varchar(30) not null ,
# `age` tinyint not null ,
# `sex` enum('m','w'));
#
# create table `class`
# (`class_id` int primary key ,
# `class_name` varchar(30) not null ,
# `score` tinyint not null ,
# tid int not null ,
# constraint tfk foreign key (tid) references teacher(teacher_id) ); #(tfk键的名字)
#
# create table `teacher`
# (`teacher_id` int primary key ,
# `teacher_name` varchar(30) not null ,
# `age` tinyint not null ,
# `doing` varchar(30) not null );
#
# create table `student1_class`
# (`s_id` int not null ,
# `c_id` int not null ,
# `class_score` tinyint not null,
# primary key (s_id,c_id),
# constraint `student1_fk` foreign key (`s_id`) references `student1`(`student1_id`),
# constraint `class_fk` foreign key (`c_id`) references `class`(`class_id`));







# create table `yonghu`
# (`yh_id` int primary key auto_increment,
# `yh_name` varchar(30) not null ,
# `yh_mima` varchar(30) not null );
#
# create table `pengyouquan`
# (`pyq_id` int primary key auto_increment,
# `pyq_tp` blob not null ,
# `pyq_nr` varchar(150) not null ,
# `pyq_dd` varchar(30) not null ,
# `pyq_sj` datetime not null );
#
# create table `pinglun`
# (`pl_id` int primary key auto_increment,
# `yh_id` int not null ,
# `pyq_id` int not null ,
# `pl_dz` bit,
# `pl_pl` text,
# constraint yh_pl foreign key (yh_id) references `yonghu`(yh_id),
# constraint pyq_pl foreign key (pyq_id) references `pengyouquan`(pyq_id));
#作业
# create table student(student_id int primary key auto_increment,student_name varchar(30) not null ,
# cla_id char(4) ,constraint cla_fk foreign key (cla_id) references class(class_id));
#
# create table course(course_id int primary key auto_increment ,course_name varchar(30) not null ,
# teach_id int ,constraint teach_fk foreign key (teach_id) references teacher(teacher_id));
#
# create table teacher(teacher_id int primary key auto_increment ,teacher_name varchar(30) not null );
#
# create table class(class_id char(4) primary key);

# create table student_course(sc_id int auto_increment,stud_id int not null ,cour_id int not null ,
# primary key (stud_id,cour_id),
# constraint stud_id foreign key (stud_id) references student(student_id),
# constraint cour_id foreign key (cour_id) references course(course_id));
#
# create table student_teacher(st_id int auto_increment,stud_id int not null ,teach_id int not null ,
# primary key (stud_id,teach_id),
# constraint stud_id foreign key (stud_id) references student(student_id),
# constraint teach_id foreign key (teach_id) references teacher(teacher_id));
#
# create table course_class(sc_id int auto_increment,cla_id int not null ,cour_id int not null ,
# primary key (cla_id,cour_id),
# constraint cla_id foreign key (cla_id) references class(class_id),
# constraint cour_id foreign key (cour_id) references course(course_id));