import math

def print_array(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j]==(None,None):
                   print("(_,_)",end='\n')
            else:
                   print (a[i][j],end='\n')
    return 
def local_distance(template_frame,test_frame):
    assert type(template_frame)==type(test_frame)==float
    return math.sqrt(pow(template_frame-test_frame,2))
def dtw(template,test):
    global_distance=0
    alignment=[]
    backpointer=[]
    empty_backpointer=(None,None)
    
    global_distance=[]
    dummy_value=-1
    for i in range(len(template)):
        this_row=[]
        for j in range(len(test)):
            this_row.append(dummy_value)
            global_distance.append(this_row)
    for i in range(len(template)):
        this_row=[]
        for i in range(len(test)):
            this_row.append(empty_backpointer)
            backpointer.append(this_row)
    
    for i in range(len(template)):
        for j in range(len(test)):
            #print("visit",i,j)
            if(i==0 and j==0):
                global_distance[i][j]=local_distance(template[i],test[j])
                backpointer[i][j]=(None,None)
            elif(i==0):
                assert global_distance[i][j-1]>=0
                global_distance[i][j]=global_distance[i][j-1]+local_distance(template[i],test[j])
                backpointer[i][j] = (i,j-1)
            elif(j==0):
                assert global_distance[i-1][j]>=0
                global_distance[i][j]=global_distance[i][j-1]+local_distance(template[i],test[j])
                backpointer[i][j] = (i-1,j)
            else:
                assert global_distance[i][j-1]>= 0
                assert global_distance[i-1][j]>= 0
                assert global_distance[i-1][j-1]>= 0 
                lowest_global_distance = global_distance[i-1][j]
                backpointer[i][j] = (i-1,j)
 
                if global_distance[i][j-1] < lowest_global_distance:
                    lowest_global_distance = global_distance[i][j-1]
                    backpointer[i][j] = (i,j-1)
 
                if global_distance[i-1][j-1] < lowest_global_distance:
                    lowest_global_distance = global_distance[i-1][j-1]
                    backpointer[i][j] = (i-1,j-1)
 
 
                global_distance[i][j] = lowest_global_distance + local_distance( template[i], test[j] )
 
    D = global_distance[len(template)-1][len(test)-1]
   # print_array(backpointer)
##    alignment=[]
##    i,j = len(template)-1 , len(test)-1
##    alignment.append( (i,j) )
##    while ( (i!=0) or (j!=0) ):
##        alignment.append(backpointer[i][j])
##        i,j = backpointer[i][j]
##    alignment.reverse()
    return D
def main():
    templates=[]
    #templates.append([-431.793436,  132.330100, -15.9079610,  21.5363992, 21.2387079,  11.8537210,  3.02862177,  4.46693419,  7.02692856, -2.68069639,  1.28214393,  0.204840285])
    templates.append( [-433.638535,  130.963651, -972.697507,  19.1314187,  8.29162537,  9.06388889 , 0.560601637, -1.18748067 , 7.02212895,  1.53924792, -4.18754399,  0.430163810])
    #templates.append( [-430.913799,  131.972308, -11.2640363,  18.4197722,  8.44263236,  8.52216316, -1.14344508, -2.73427688,   6.02651969,  0.223774779, -4.55366075, -0.207651836])
    #test =          ( [-429.061365,  133.575464, -9.59183315,  18.5131113,  9.61025012,  8.91053387, -0.114767068,  0.651277137, 6.06627884, -0.430636894, -3.36932415, -0.931676451])
    #template=([3,2,1,2,3])
    test=( [-433.638535,  130.963651, -972.697507,  19.1314187,  8.29162537,  9.06388889 , 0.560601637, -1.18748067 , 7.02212895,  1.53924792, -4.18754399,  0.430163810])

    for t in templates:
        D= dtw(t, test)
        print( "for same persons same samples", D)
   # for (i,j) in alignment:
       # print ("Alignment",(i,j),": ",t[i]," aligns with", test[j])
if __name__=='__main__':
    main()
