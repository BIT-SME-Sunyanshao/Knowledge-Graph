# cmd管理员身份输入neo4j.bat console
# MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r
# match (n) detach delete n
# 复制上述CQL代码，在网页端清除所有节点和边
from py2neo import Graph, Node, Relationship

graph = Graph('http://localhost:7474', auth=('neo4j', '123456'))

'''
1.创建节点
'''

# 分离系统
sep_system = Node("分离系统", name="分离系统")
sep_system1 = Node("分离系统", name="一二级分离系统")

# 信号转化装置
signal_conv_device = Node("信号转化装置", name="信号转化装置")
signal_conv_device1 = Node("信号转化装置", name="电点火器A",
                           质量="2.5kg", 成本="300", 性能="0.99970", 作用时间="20ms", 输出功率="12.5MPa")
signal_conv_device2 = Node("信号转化装置", name="电点火器B",
                           质量="2.72kg", 成本="275", 性能="0.99962", 作用时间="30ms", 输出功率="14.5MPa")
signal_conv_device3 = Node("信号转化装置", name="电起爆器A",
                           质量="1.8kg", 成本="340", 性能="0.99974", 作用时间="15ms", 输出功率="10MPa")
signal_conv_device4 = Node("信号转化装置", name="电起爆器B",
                           质量="2.3kg", 成本="350", 性能="0.99986", 作用时间="20ms", 输出功率="12MPa")
signal_conv_device5 = Node("信号转化装置", name="半导体桥点火器",
                           质量="0.8kg", 成本="500", 性能="0.99990", 作用时间="1ms", 输出功率="12MPa")
signal_conv_device6 = Node("信号转化装置", name="机械起爆器",
                           质量="2.94kg", 成本="280", 性能="0.99957", 作用时间="30ms", 输出功率="10MPa")
signal_conv_device7 = Node("信号转化装置", name="隔板起爆器",
                           质量="2.4kg", 成本="320", 性能="0.9998", 作用时间="1ms", 输出功率="13MPa")
signal_conv_device8 = Node("信号转化装置", name="延期点火器",
                           质量="1.6kg", 成本="290", 性能="0.99940", 作用时间="26ms", 输出功率="11MPa")

# 信号传递装置
signal_trans_device = Node("信号传递装置", name="信号传递装置")
signal_trans_device1 = Node("信号传递装置", name="限制性导爆组件A",
                            质量="0.03kg/m", 成本="60", 性能="0.99943", 载荷="13MP", 传递速度="7000m/s")
signal_trans_device2 = Node("信号传递装置", name="限制性导爆组件B",
                            质量="0.025kg/m", 成本="50", 性能="0.99951", 载荷="11MP", 传递速度="2000m/s")
signal_trans_device3 = Node("信号传递装置", name="塑料导爆管组件A",
                            质量="0.02kg/m", 成本="100", 性能="0.99961", 载荷="12.8MP", 传递速度="1600m/s")
signal_trans_device4 = Node("信号传递装置", name="塑料导爆管组件B",
                            质量="0.023kg/m", 成本="120", 性能="0.99972", 载荷="13MP", 传递速度="1800m/s")

# 分离装置
separation_device = Node("分离装置", name="分离装置")
separation_device1 = Node("分离装置", name="爆炸螺栓A",
                          质量="0.36kg", 成本="27", 性能="0.99968", 污染量="5mg", 承载能力="110kN", 分离时间="2ms")
separation_device2 = Node("分离装置", name="爆炸螺栓B",
                          质量="0.38kg", 成本="30", 性能="0.99981", 污染量="4mg", 承载能力="81kN", 分离时间="3ms")
separation_device3 = Node("分离装置", name="爆炸螺栓C",
                          质量="0.3kg", 成本="22", 性能="0.99972", 污染量="4mg", 承载能力="70kN", 分离时间="1.5ms")
separation_device4 = Node("分离装置", name="爆炸螺栓D",
                          质量="0.14kg", 成本="45", 性能="0.99982", 污染量="2mg", 承载能力="120kN", 分离时间="0.4ms")
separation_device5 = Node("分离装置", name="爆炸螺栓E",
                          质量="0.43kg", 成本="65", 性能="0.99985", 污染量="5mg", 承载能力="150kN", 分离时间="20ms")

separation_device6 = Node("分离装置", name="分离螺母A",
                          质量="0.3kg", 成本="70", 性能="0.99972", 污染量="3mg", 承载能力="90kN")
separation_device7 = Node("分离装置", name="爆炸螺栓B",
                          质量="0.2kg", 成本="60", 性能="0.99968", 污染量="4mg", 承载能力="85kN")
separation_device8 = Node("分离装置", name="爆炸螺栓C",
                          质量="0.12kg", 成本="50", 性能="0.99957", 污染量="3mg", 承载能力="80kN")
separation_device9 = Node("分离装置", name="连接销式分离装置A",
                          质量="0.35kg", 成本="38", 性能="0.99969", 污染量="0.36mg", 承载能力="75kN")
separation_device10 = Node("分离装置", name="连接销式分离装置B",
                           质量="0.25kg", 成本="25", 性能="0.9996", 污染量="3mg", 承载能力="72kN")

# 动力作动装置
power_actuator = Node("动力作动装置", name="动力作动装置")
power_actuator1 = Node("动力作动装置", name="火工作动筒A",
                       质量="11kg", 成本="5880", 性能="0.99965", 推力="30kN", 工作时间="60ms")
power_actuator2 = Node("动力作动装置", name="火工作动筒B",
                       质量="13kg", 成本="6050", 性能="0.99971", 推力="35kN", 工作时间="75ms")
power_actuator3 = Node("动力作动装置", name="火工作动筒C",
                       质量="14.3kg", 成本="6310", 性能="0.99964", 推力="36kN", 工作时间="70ms")
power_actuator4 = Node("动力作动装置", name="分离火箭A",
                       质量="7kg", 成本="5500", 性能="0.99989", 推力="13.2kN", 工作时间="600ms")
power_actuator5 = Node("动力作动装置", name="分离火箭B",
                       质量="9.5kg", 成本="6000", 性能="0.99978", 推力="16.8kN", 工作时间="480ms")
power_actuator6 = Node("动力作动装置", name="分离火箭C",
                       质量="8.9kg", 成本="5730", 性能="0.99976", 推力="15kN", 工作时间="500ms")

# 功能
function1 = Node("功能", name="连接与解锁")
function2 = Node("功能", name="提供推力")
function3 = Node("功能", name="提供分离冲量")
function4 = Node("功能", name="点火")
function5 = Node("功能", name="起爆")
function6 = Node("功能", name="延时")
function7 = Node("功能", name="切割与破碎")
function8 = Node("功能", name="阀门打开或关闭")
function9 = Node("功能", name="信号转化")
function10 = Node("功能", name="信号传递")
function11 = Node("功能", name="控制")
function12 = Node("功能", name="执行")

# 任务目标
task1 = Node("任务目标", name="登月")
task2 = Node("任务目标", name="进入近地轨道")
task3 = Node("任务目标", name="离开地球轨道")
task4 = Node("任务目标", name="进入绕月轨道")
task5 = Node("任务目标", name="离开地球轨道")

task6 = Node("任务目标", name="一二级分离")
task7 = Node("任务目标", name="星箭分离")
task8 = Node("任务目标", name="有效载荷舱分离")
task9 = Node("任务目标", name="整流罩分离")

'''
2.创建关系
'''
# 分离系统有各个子系统（分离系统->一二级分离系统）
has_subsystem1 = Relationship(sep_system, "has_subsystem", sep_system1)

# 子系统有各个架构（一二级分离系统->信号转化装置）
has_architecture1 = Relationship(sep_system1, "has_architecture", signal_conv_device)
has_architecture2 = Relationship(sep_system1, "has_architecture", signal_trans_device)
has_architecture3 = Relationship(sep_system1, "has_architecture", separation_device)
has_architecture4 = Relationship(sep_system1, "has_architecture", power_actuator)

# 架构有各种选项（信号转化装置->电点火器A）
has_option1 = Relationship(signal_conv_device, "has_option", signal_conv_device1)
has_option2 = Relationship(signal_conv_device, "has_option", signal_conv_device2)
has_option3 = Relationship(signal_conv_device, "has_option", signal_conv_device3)
has_option4 = Relationship(signal_conv_device, "has_option", signal_conv_device4)
has_option5 = Relationship(signal_conv_device, "has_option", signal_conv_device5)
has_option6 = Relationship(signal_conv_device, "has_option", signal_conv_device6)
has_option7 = Relationship(signal_conv_device, "has_option", signal_conv_device7)
has_option8 = Relationship(signal_conv_device, "has_option", signal_conv_device8)

# 架构有各种选项（信号传递装置->限制性导爆组件A）
has_option9 = Relationship(signal_trans_device, "has_option", signal_trans_device1)
has_option10 = Relationship(signal_trans_device, "has_option", signal_trans_device2)
has_option11 = Relationship(signal_trans_device, "has_option", signal_trans_device3)
has_option12 = Relationship(signal_trans_device, "has_option", signal_trans_device4)

# 架构有各种选项（分离装置->爆炸螺栓A）
has_option13 = Relationship(separation_device, "has_option", separation_device1)
has_option14 = Relationship(separation_device, "has_option", separation_device2)
has_option15 = Relationship(separation_device, "has_option", separation_device3)
has_option16 = Relationship(separation_device, "has_option", separation_device4)
has_option17 = Relationship(separation_device, "has_option", separation_device5)
has_option18 = Relationship(separation_device, "has_option", separation_device6)
has_option19 = Relationship(separation_device, "has_option", separation_device7)
has_option20 = Relationship(separation_device, "has_option", separation_device8)
has_option21 = Relationship(separation_device, "has_option", separation_device9)
has_option22 = Relationship(separation_device, "has_option", separation_device10)

# 架构有各种选项（动力作动装置->火工作动筒A）
has_option23 = Relationship(power_actuator, "has_option", power_actuator1)
has_option24 = Relationship(power_actuator, "has_option", power_actuator2)
has_option25 = Relationship(power_actuator, "has_option", power_actuator3)
has_option26 = Relationship(power_actuator, "has_option", power_actuator4)
has_option27 = Relationship(power_actuator, "has_option", power_actuator5)
has_option28 = Relationship(power_actuator, "has_option", power_actuator6)

# 架构有某种功能（爆炸螺栓A->连接与解锁）
# 信号转化装置，有功能，转化信号
has_function1 = Relationship(signal_conv_device1, "has_function", function9)
has_function2 = Relationship(signal_conv_device2, "has_function", function9)
has_function3 = Relationship(signal_conv_device3, "has_function", function9)
has_function4 = Relationship(signal_conv_device4, "has_function", function9)
has_function5 = Relationship(signal_conv_device5, "has_function", function9)
has_function6 = Relationship(signal_conv_device6, "has_function", function9)
has_function7 = Relationship(signal_conv_device7, "has_function", function9)
has_function8 = Relationship(signal_conv_device8, "has_function", function9)
has_function9 = Relationship(signal_conv_device, "has_function", function9)

# 信号传递装置，有功能，传递信号
has_function10 = Relationship(signal_trans_device1, "has_function", function10)
has_function11 = Relationship(signal_trans_device2, "has_function", function10)
has_function12 = Relationship(signal_trans_device3, "has_function", function10)
has_function13 = Relationship(signal_trans_device4, "has_function", function10)
has_function14 = Relationship(signal_trans_device, "has_function", function10)

# 分离装置，有功能，连接与解锁
has_function15 = Relationship(separation_device1, "has_function", function1)
has_function16 = Relationship(separation_device2, "has_function", function1)
has_function17 = Relationship(separation_device3, "has_function", function1)
has_function18 = Relationship(separation_device4, "has_function", function1)
has_function19 = Relationship(separation_device5, "has_function", function1)
has_function20 = Relationship(separation_device6, "has_function", function1)
has_function21 = Relationship(separation_device7, "has_function", function1)
has_function22 = Relationship(separation_device8, "has_function", function1)
has_function23 = Relationship(separation_device9, "has_function", function1)
has_function24 = Relationship(separation_device10, "has_function", function1)
has_function25 = Relationship(separation_device, "has_function", function1)

# 动力作动装置，有功能，提供分离冲量
has_function26 = Relationship(power_actuator1, "has_function", function3)
has_function27 = Relationship(power_actuator2, "has_function", function3)
has_function28 = Relationship(power_actuator3, "has_function", function3)
has_function29 = Relationship(power_actuator4, "has_function", function3)
has_function30 = Relationship(power_actuator5, "has_function", function3)
has_function31 = Relationship(power_actuator6, "has_function", function3)
has_function32 = Relationship(power_actuator, "has_function", function3)

# 功能实现某项任务目标
achieve1 = Relationship(function1, "achieve", task6)
achieve2 = Relationship(function2, "achieve", task6)
achieve3 = Relationship(function3, "achieve", task6)
achieve4 = Relationship(function4, "achieve", task6)
achieve5 = Relationship(function5, "achieve", task6)
achieve6 = Relationship(function6, "achieve", task6)
achieve7 = Relationship(function7, "achieve", task6)
achieve8 = Relationship(function8, "achieve", task6)
achieve9 = Relationship(function9, "achieve", task6)
achieve10 = Relationship(function10, "achieve", task6)
achieve11 = Relationship(function11, "achieve", task6)
achieve12 = Relationship(function12, "achieve", task6)

'''
3.创建图谱
'''
# 系统、子系统
graph.merge(sep_system, "分离系统", "name")
graph.merge(sep_system1, "分离系统", "name")

# 信号转化装置
graph.merge(signal_conv_device1, "信号转化装置", "name")
graph.merge(signal_conv_device2, "信号转化装置", "name")
graph.merge(signal_conv_device3, "信号转化装置", "name")
graph.merge(signal_conv_device4, "信号转化装置", "name")
graph.merge(signal_conv_device5, "信号转化装置", "name")
graph.merge(signal_conv_device6, "信号转化装置", "name")
graph.merge(signal_conv_device7, "信号转化装置", "name")
graph.merge(signal_conv_device8, "信号转化装置", "name")

# 信号传递装置
graph.merge(signal_trans_device1, "信号传递装置", "name")
graph.merge(signal_trans_device2, "信号传递装置", "name")
graph.merge(signal_trans_device3, "信号传递装置", "name")
graph.merge(signal_trans_device4, "信号传递装置", "name")

# 分离装置
graph.merge(separation_device1, "分离装置", "name")
graph.merge(separation_device2, "分离装置", "name")
graph.merge(separation_device3, "分离装置", "name")
graph.merge(separation_device4, "分离装置", "name")
graph.merge(separation_device5, "分离装置", "name")
graph.merge(separation_device6, "分离装置", "name")
graph.merge(separation_device7, "分离装置", "name")
graph.merge(separation_device8, "分离装置", "name")
graph.merge(separation_device9, "分离装置", "name")
graph.merge(separation_device10, "分离装置", "name")

# 动力作动装置
graph.merge(power_actuator1, "动力作动装置", "name")
graph.merge(power_actuator2, "动力作动装置", "name")
graph.merge(power_actuator3, "动力作动装置", "name")
graph.merge(power_actuator4, "动力作动装置", "name")
graph.merge(power_actuator5, "动力作动装置", "name")
graph.merge(power_actuator6, "动力作动装置", "name")

# 功能
graph.merge(function1, "功能", "name")
graph.merge(function2, "功能", "name")
graph.merge(function3, "功能", "name")
graph.merge(function4, "功能", "name")
graph.merge(function5, "功能", "name")
graph.merge(function6, "功能", "name")
graph.merge(function7, "功能", "name")
graph.merge(function8, "功能", "name")
graph.merge(function9, "功能", "name")
graph.merge(function10, "功能", "name")
graph.merge(function11, "功能", "name")
graph.merge(function12, "功能", "name")

# 任务目标
graph.merge(task1, "任务目标", "name")
graph.merge(task2, "任务目标", "name")
graph.merge(task3, "任务目标", "name")
graph.merge(task4, "任务目标", "name")
graph.merge(task5, "任务目标", "name")
graph.merge(task6, "任务目标", "name")
graph.merge(task7, "任务目标", "name")
graph.merge(task8, "任务目标", "name")
graph.merge(task9, "任务目标", "name")

# 关系
graph.merge(has_subsystem1, "分离系统", "name")

graph.merge(has_architecture1, "分离系统", "name")
graph.merge(has_architecture2, "分离系统", "name")
graph.merge(has_architecture3, "分离系统", "name")
graph.merge(has_architecture4, "分离系统", "name")

graph.merge(has_option1, "信号转化装置", "name")
graph.merge(has_option2, "信号转化装置", "name")
graph.merge(has_option3, "信号转化装置", "name")
graph.merge(has_option4, "信号转化装置", "name")
graph.merge(has_option5, "信号转化装置", "name")
graph.merge(has_option6, "信号转化装置", "name")
graph.merge(has_option7, "信号转化装置", "name")
graph.merge(has_option8, "信号转化装置", "name")

graph.merge(has_option9, "信号传递装置", "name")
graph.merge(has_option10, "信号传递装置", "name")
graph.merge(has_option11, "信号传递装置", "name")
graph.merge(has_option12, "信号传递装置", "name")

graph.merge(has_option13, "分离装置", "name")
graph.merge(has_option14, "分离装置", "name")
graph.merge(has_option15, "分离装置", "name")
graph.merge(has_option16, "分离装置", "name")
graph.merge(has_option17, "分离装置", "name")
graph.merge(has_option18, "分离装置", "name")
graph.merge(has_option19, "分离装置", "name")
graph.merge(has_option20, "分离装置", "name")
graph.merge(has_option21, "分离装置", "name")
graph.merge(has_option22, "分离装置", "name")

graph.merge(has_option23, "动力作动装置", "name")
graph.merge(has_option24, "动力作动装置", "name")
graph.merge(has_option25, "动力作动装置", "name")
graph.merge(has_option26, "动力作动装置", "name")
graph.merge(has_option27, "动力作动装置", "name")
graph.merge(has_option28, "动力作动装置", "name")

graph.merge(has_function1, "信号转化装置", "name")
graph.merge(has_function2, "信号转化装置", "name")
graph.merge(has_function3, "信号转化装置", "name")
graph.merge(has_function4, "信号转化装置", "name")
graph.merge(has_function5, "信号转化装置", "name")
graph.merge(has_function6, "信号转化装置", "name")
graph.merge(has_function7, "信号转化装置", "name")
graph.merge(has_function8, "信号转化装置", "name")
graph.merge(has_function9, "信号转化装置", "name")

graph.merge(has_function10, "信号传递装置", "name")
graph.merge(has_function11, "信号传递装置", "name")
graph.merge(has_function12, "信号传递装置", "name")
graph.merge(has_function13, "信号传递装置", "name")
graph.merge(has_function14, "信号传递装置", "name")

graph.merge(has_function15, "分离装置", "name")
graph.merge(has_function16, "分离装置", "name")
graph.merge(has_function17, "分离装置", "name")
graph.merge(has_function18, "分离装置", "name")
graph.merge(has_function19, "分离装置", "name")
graph.merge(has_function20, "分离装置", "name")
graph.merge(has_function21, "分离装置", "name")
graph.merge(has_function22, "分离装置", "name")
graph.merge(has_function23, "分离装置", "name")
graph.merge(has_function24, "分离装置", "name")
graph.merge(has_function25, "分离装置", "name")

graph.merge(has_function26, "动力作动装置", "name")
graph.merge(has_function27, "动力作动装置", "name")
graph.merge(has_function28, "动力作动装置", "name")
graph.merge(has_function29, "动力作动装置", "name")
graph.merge(has_function30, "动力作动装置", "name")
graph.merge(has_function31, "动力作动装置", "name")
graph.merge(has_function32, "动力作动装置", "name")

graph.merge(achieve1, "功能", "name")
graph.merge(achieve3, "功能", "name")
graph.merge(achieve9, "功能", "name")
graph.merge(achieve10, "功能", "name")