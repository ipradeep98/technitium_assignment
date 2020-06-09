import re
import pprint
#cost inputs
NY_cost={'L':120,'XL':230,'2XL':450,'4XL':774,'8XL':1400,'10XL':2820}
Ind_cost = {'L':140,'2XL':413,'4XL':890,'8XL':1300,'10XL':2970}
China_cost = {'L':110,'XL':200,'4XL':670,'8XL':1180}
#NewYork region
def NewYorkCost(power,hours):
    units={'10XL':320,'8XL':160,'4XL':80,'2XL':40,'XL':20,'L':10}
    NewYorkCost.final1={}
    NewYorkCost.final1['region']='New York'
    count={}
    power_sub=power
    list_1=list(units.keys())
    k=0
    for i in units.keys():
        if k+1<len(list_1):
            if NY_cost[list_1[k]]<=(NY_cost[list_1[k+1]])*2:
                power_util=units[i]
                j=0
                while power_util<=power_sub:
                    count[i]=j+1
            
                    power_util=power_util+units[i]
                    rem_power=power_sub-power_util
            
                    if rem_power>0:
                        j+=1
                if rem_power<0:
                    power_sub=rem_power+units[i]
                rem_power=0
            k+=1
        else:
            power_util=units[i]
            j=0
            while power_util<=power_sub:
                count[i]=j+1        
                power_util=power_util+units[i]
                rem_power=power_sub-power_util
            
                if rem_power>0:
                    j+=1
            if rem_power<0:
                power_sub=rem_power+units[i]
            rem_power=0
    final_list = [(k, v) for k, v in count.items()]
    NewYorkCost.final1['machines']=final_list
    finalcost=0
    for i in count.keys():
        cal_cost=count[i]*NY_cost[i]*hours
        finalcost=finalcost+cal_cost
    NewYorkCost.final1['total_cost']='${}'.format(finalcost)
#India region
def IndiaCost(power,hours):
    units={'10XL':320,'8XL':160,'4XL':80,'2XL':40,'L':10}
    count={}
    IndiaCost.final2={}
    IndiaCost.final2['region']='India'
    power_sub=power
    list_1=list(units.keys())
    k=0
    for i in units.keys():
        if k+1<len(list_1):
            if Ind_cost[list_1[k]]<=(Ind_cost[list_1[k+1]])*2:
                power_util=units[i]
                j=0
                while power_util<=power_sub:
                    count[i]=j+1
                    power_util=power_util+units[i]
                    rem_power=power_sub-power_util
            
                    if rem_power>0:
                        j+=1
                if rem_power<0:
                    power_sub=rem_power+units[i]
                rem_power=0
            k+=1
        else:
            power_util=units[i]
            j=0
            while power_util<=power_sub:
                count[i]=j+1        
                power_util=power_util+units[i]
                rem_power=power_sub-power_util
            
                if rem_power>=0:
                    j+=1
            if rem_power<0:
                power_sub=rem_power+units[i]
            rem_power=0
    final_list = [(k, v) for k, v in count.items()]
    IndiaCost.final2['machines']=final_list
    finalcost=0
    for i in count.keys():
        cal_cost=count[i]*Ind_cost[i]*hours
        finalcost=finalcost+cal_cost
    IndiaCost.final2['total_cost']='${}'.format(finalcost)
#China region
def ChinaCost(power,hours):
    final_result={}
    units={'8XL':160,'4XL':80,'XL':20,'L':10}
    final3={}
    final3['region']='China'
    count={}
    power_sub=power
    list_1=list(units.keys())
    k=0
    for i in units.keys():
        if k+1<len(list_1):
            if China_cost[list_1[k]]<=(China_cost[list_1[k+1]])*2:
                power_util=units[i]
                j=0
                while power_util<=power_sub:
                    count[i]=j+1
            
                    power_util=power_util+units[i]
                    rem_power=power_sub-power_util
            
                    if rem_power>0:
                        j+=1
                if rem_power<0:
                    power_sub=rem_power+units[i]
                rem_power=0
            k+=1
        else:
            power_util=units[i]
            j=0
            while power_util<=power_sub:
                count[i]=j+1        
                power_util=power_util+units[i]
                rem_power=power_sub-power_util
            
                if rem_power>0:
                    j+=1
            if rem_power<0:
                power_sub=rem_power+units[i]
            rem_power=0
    final_list = [(k, v) for k, v in count.items()]
    final3['macines']=final_list
    finalcost=0
    for i in count.keys():
        cal_cost=count[i]*China_cost[i]*hours
        finalcost=finalcost+cal_cost
    final3['total_cost']='${}'.format(finalcost)
    dall = []
    for d in [NewYorkCost.final1, IndiaCost.final2, final3]:
      dall.append(d)
    final_result['Output']=dall
    pprint.pprint(final_result)
#input 
str1='Capacity of 1150 units for 1 Hour'
get_inputs = re.findall(r'\d+', str1)
res = list(map(int, get_inputs))
power=res[0]
hours=res[1]
#function call
NewYorkCost(power,hours)
IndiaCost(power,hours)
ChinaCost(power,hours)
    
