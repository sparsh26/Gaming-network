def create_data_structure(string_input):
    dic,num,k={},0,[]
    p=string_input.split('.')
    for e in p:
        l=e.split()
        for i in range(1,len(l)):
            l.pop()    
        for i in l:
         if i not in dic:
                dic[i]={'games':[],'connections':[]}
         num=e.find('to')
         c=e.find('play',num+1)   
         if c==-1:
                m=e[num+len('to')+1:]  
                dic[i]['connections']=m.split(', ')
         if c!=-1:
             s=e[c+len('play')+1:]
             dic[i]['games']=s.split(', ')
         
    network=dic
    return network
    
def get_connections(network, user):
    if user in network:
       return network[user]['connections']
    return None  
	

def get_games_liked(network,user):
    if user in network:
        return network[user]['games']
    return None
        
        
def add_connection(network, user_A, user_B):
  if user_A in network and user_B in network:     
     for e in network[user_A]['connections']:
        if e not in network[user_B]['connections'] or e!=user_B:
           network[user_B]['connections'].append(e)
     if user_B not in network[user_A]['connections']:
            network[user_A]['connections'].append(user_B) 
     return network
  return False 
	
def add_new_user(network, user, games):
    if user not in network:
      network[user]={'games':games,'connections':[]}
    return network
		
		
def get_secondary_connections(network, user):
    l=[]
    for e in network[user]['connections']:
        l=l+network[e]['connections']
    return l

    
def connections_in_common(network, user_A, user_B):
    l=[]
    for e in network[user_A]['connections']:
        if e in network[user_B]['connections']:
            l.append(e)
    return len(l)
    
def find_path_to_friend(network, user_A, user_B):
  if user_A not in network or user_B not in network:
        return None
  l,p=[user_A],[user_A]
  a=user_A        
  for e in network[user_A]['connections']:
        if user_B in network[e]['connections']:
            return [user_A,e,user_B]
  c=finding_path(network,user_A,user_B,p,a)
  if is_list(c):
        return c
  return None
  
def is_list(p):
    return isinstance(p, list)
    
#Helps in finding the path(longest path in bigger paths)
def finding_path(network,user_A,user_B,p,a):
    s=0
    for e in network[user_A]['connections']:
        if user_B in network[e]['connections']:
            return [a,user_A,e,user_B]
    if user_B in network[user_A]['connections']:
        p=p+[user_B]
        return p
    for e in network[user_A]['connections']:
        if s==1:
            if e in network[a]['connections']:
                return p
                p.pop()
                s=0
        if e in p or e==user_A:
          continue    
        p.append(e)
        r=finding_path(network,e,user_B,p,a)
        if r==0:
            p,s=[a,user_A],1
            continue
        return union(p,r)    
    return 0
 
def union(a,b):
 for e in b:
  if e not in a:
   a.append(e)
 return a     
    
def most_popular_game(network,user_A):
    #aim to find the most popular game in the user's connections(including connections of connections)
    count,l,maxi,game={},[],0,'s'
    final=find_game(network,user_A,count,l)
    #final deciding the most popular game
    for e in final:
        if final[e]>maxi:
            maxi=final[e]
            game=e
    return game

def find_game(network,user_A,count,l):
   l.append(user_A)
   #rates the games for an individual user
   for e in network[user_A]['games']:
      if e not in count:
          count[e]=1
      else:
          count[e]+=1
   #rating games for connections without any connection or the user being repeated
   for i in network[user_A]['connections']:
       if i in l:
          continue
       return find_game(network,i,count,l)                 
   return count     



example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."
    
net = create_data_structure(example_input)
#print net
#print get_connections(net, "Debra")
#print get_connections(net, "Mercede")
#print get_games_liked(net, "John")
#print add_connection(net, "John", "Freda")
#print add_new_user(net, "nick", []) 
#print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
#print get_secondary_connections(net, "Mercedes")
#print connections_in_common(net, "Mercedes", "John")
print find_path_to_friend(net, "John", "Robin")