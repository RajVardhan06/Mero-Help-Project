def add_edge(adj, src, dest):
 
    adj[src].append(dest);
    adj[dest].append(src);
  

def BFS(adj, src, dest, v, pred, dist):
    queue = []
    visited = [False for i in range(v)];
  
    for i in range(v):
 
        dist[i] = 1000000
        pred[i] = -1;
     
    
    visited[src] = True;
    dist[src] = 0;
    queue.append(src);

    while (len(queue) != 0):
        u = queue[0];
        queue.pop(0);
        for i in range(len(adj[u])):
         
            if (visited[adj[u][i]] == False):
                visited[adj[u][i]] = True;
                dist[adj[u][i]] = dist[u] + 1;
                pred[adj[u][i]] = u;
                queue.append(adj[u][i]);
                if (adj[u][i] == dest):
                    return True;
  
    return False;

def printShortestDistance(adj, s, dest, v):
    pred=[0 for i in range(v)]
    dist=[0 for i in range(v)];
  
    if (BFS(adj, s, dest, v, pred, dist) == False):
        print("Given source and destination are not connected")
  
    
    path = []
    crawl = dest;
    path.append(crawl);
     
    while (pred[crawl] != -1):
        path.append(pred[crawl]);
        crawl = pred[crawl];
     
    return path
         


gl=['Silk Institute', 'Thalaghattapura', 'Vajarahalli',
 'Doddakallasandra', 'Konankunte Cross', 'Yelachenahalli',
  'Jaya Prakash Nagar', 'Banashankari',
   'Rashtreeya Vidyalaya Road', 'Jayanagar', 'South End Circle',
    'Lalbagh', 'National College', 'Krishna Rajendra Market', 'Chickpete',
     'Nadaprabhu Kempegowda Station, Majestic', 'Mantri Square Sampige Road',
      'Srirampura', 'Mahakavi Kuvempu Road', 'Rajajinagar', 'Mahalakshmi',
       'Sandal Soap Factory', 'Yeshwanthpur', 'Goragunte Palya', 'Peenya',
        'Peenya Industry', 'Jalahalli', 'Dasarahalli', 'Nagasandra']
pl=['Kengeri', 'Kengeri Bus Terminal', 'Pattanagere', 'Jnanabharathi',
 'Rajarajeshwari Nagar', 'Nayandahalli', 'Mysuru Road', 'Deepanjali Nagar',
  'Attiguppe', 'Vijayanagar', 'Balagangadaranatha Swamiji Station, Hosahalli',
   'Magadi Road', 'Krantivira Sangolli Rayanna Railway Station',
    'Nadaprabhu Kempegowda Station, Majestic', 'Sir M. Visvesvaraya Station, Central College',
     'Dr. B.R. Ambedkar Station, Vidhana Soudha', 'Cubbon Park', 'Mahatma Gandhi Road',
      'Trinity', 'Halasuru', 'Indiranagar', 'Swami Vivekananda Road', 'Baiyappanahalli']
ll=[gl,pl]

source=input('Enter the source:')
dest=input('Enter the destination:')

source=source.strip().title()
dest=dest.strip().title()

if source.lower()=='majestic':
    source='Nadaprabhu Kempegowda Station, Majestic'
elif source.lower()=='jp nagar':
    source='Jaya Prakash Nagar'
elif source.lower()=='kr market':
    source='Krishna Rajendra Market'
elif source.lower() == 'hosahalli':
    source = 'Balagangadaranatha Swamiji Station, Hosahalli'
elif source.lower() == 'mg road':
    source = 'Mahatma Gandhi Road'
elif source.lower() == 'mantri square':
    source = 'Mantri Square Sampige Road'
elif source.lower() == 'rr nagar':
    source = 'Rajarajeshwari Nagar'

    
    
if dest.lower()=='majestic':
    dest='Nadaprabhu Kempegowda Station, Majestic'
elif dest.lower()=='jp nagar':
    dest='Jaya Prakash Nagar'
elif dest.lower()=='kr market':
    dest='Krishna Rajendra Market'
elif dest.lower() == 'hosahalli':
    dest = 'Balagangadaranatha Swamiji Station, Hosahalli'
elif dest.lower() == 'mg road':
    dest = 'Mahatma Gandhi Road'
elif dest.lower() == 'mantri square':
    dest = 'Mantri Square Sampige Road'
elif dest.lower() == 'rr nagar':
    dest = 'Rajarajeshwari Nagar'



if source=='' or dest=='':
    print()
    print('PLEASE MAKE SURE TO ENTER BOTH THE FIELDS...')

elif source not in gl+pl or dest not in gl+pl:
    print()
    print('STATION NAME INVALID. PLEASE ENTER THE STATION NAMES CORRECTLY...') 

else:
    alll=[gl,pl]
    gd={}
    pd={}
    for i in gl :
        ind=gl.index(i)
        if ind==0:
            d={gl[ind+1]:1}
            gd[i]=d
        elif ind==len(gl)-1 :
            d={gl[ind-1]:1}
            gd[i]=d
        elif ind!=0 and ind!=len(gl)-1:
            d={gl[ind+1]:1,gl[ind-1]:1}
            gd[i]=d


    for i in pl :
        ind=pl.index(i)
        if ind==0:
            d={pl[ind+1]:1}
            pd[i]=d
        elif ind==len(pl)-1 :
            d={pl[ind-1]:1}
            pd[i]=d
        elif ind!=0 and ind!=len(gl)-1:
            d={pl[ind+1]:1,pl[ind-1]:1}
            pd[i]=d


    graph={}
    for i in gd :
        if i in pd :
            gd[i].update(pd[i])
            graph[i]=gd[i]

    gd.update(pd)

    for i in gd :
        if i not in graph :
            graph[i]=gd[i]


    d={}
    stations=[]


    for i in gl+pl:
        if i not in stations:
            stations.append(i)
    sn=len(stations)

    for i in stations:
        d[i]=stations.index(i)


    adj=[[] for i in range(sn)]

    for i in stations:
        for j in graph[i]:
            x=stations.index(i)
            y=stations.index(j)
            add_edge(adj,x,y)

    print()


    

    sno=d[source]
    eno=d[dest]



    a=printShortestDistance(adj, sno, eno, sn)
    stpath=[]
    for i in a :
        stpath.append(stations[i])
    stpath=stpath[::-1]




    def drc(a,b,lst):
        if lst.index(b)>lst.index(a):
            return 'up'
        else:
            return 'down'
        

    for i in ll:
        if source in i and dest in i :
            print()
            print('The shortest path:')
            for j in stpath:
                print(j)
                if stpath.index(j)<len(stpath)-1:
                    print('|') 
            print('==================')
            
            print(f'You will need to go through a total of {len(stpath)-2} stations. ')

            print('==================')
            
            
            if i.index(source) > i.index(dest) :
                if i==gl:
                    print('Please board the Green line train towards',i[0])
                else:
                    print('PLease board the Purple line train towards',i[0])
            else:
                if i==gl:
                    print('Please board the Green line train towards',i[-1])
                else:
                    print('Please board the purple line train towards',i[-1])
            
            print('No line change is required.')
            print('Get off at',dest)
            
            print('==================')
            
            print('It will take approximately:',2*len(stpath),'minutes to reach your destination.')
            
            print('==================')
            
            print('Have a safe journey!')       
            break 


    else :
        for i in ll:
            if source in i and dest not in i:
                sline=i
            if dest in i and source not in i:
                eline=i
        for j in sline :
            if j in eline :
                c=j
        print()
        print('The shortest path:')
        
        for y in stpath:
            print(y)
            if stpath.index(y)<len(stpath)-1:
                print('|') 
        
        print('==================')
        
        print(f'You will need to go through a total of {len(stpath)-2} stations. ')

        print('==================')
        
        if sline==pl:
            if drc(source,c,pl)=='up':
                print('Please board the purple line train towards',pl[-1])        
            else:
                print('Please board the purple line train towards',pl[0])
        else:
            if drc(source,c,gl)=='up':
                print('Please board the Green line train towards',gl[-1])
                    
            else:
                print('Please board the Green line train towards',gl[0])
        
        sind=sline.index(source)
        dind=eline.index(dest)
        csind=sline.index(c)
        ceind=eline.index(c)
        sd=csind-sind-1
        ed=ceind-dind-1
        if abs(ed)==0:
            x=1
        else:
            x=abs(ed)
        
        
        print(f'travel for {abs(sd)} stations.')
        print('Get off the train and change lines at',c) 
        
        if sline==gl:
            if drc(c,dest,pl)=='up':
                print('Please board the purple line train towards',pl[-1])        
            else:
                print('Please board the purple line train towards',pl[0])
        else:
            if drc(c,dest,gl)=='up':
                print('Please board the Green line train towards',gl[-1])
                    
            else:
                print('Please board the Green line train towards',gl[0])
        
        
        
           
        print(f'Travel another {x} stations and get off at {dest}')
        
        print('==================')
        
        print(f'It will take approximately {2*len(stpath)+0.5*len(stpath)} minutes to reach the destination.')
        
        print('==================')
        
        print('Have a safe journey!')
        print()
        
        
        
        