
import numpy, itertools, string
letters =string.ascii_lowercase
letters =list(letters)
lttrs=[letters[i] for i in [0,1,2]]
print(lttrs)
def which_is_true(indexTF):
    return [i for i, x in enumerate(indexTF) if x]

  
def index_TF(x,index=[True]):
    if(len(index)<len(x)):
        index_final=list(itertools.islice(itertools.cycle(index), len(x)))
    else:
        index_final=index[:len(x)]
    return [x[i] for i in list(which_is_true(index_final))]


def rep_times(x, times=1,each=1):
    result_numpy=numpy.repeat(x,each)
    result_itertools=list(itertools.repeat(result_numpy,times))
    return list(itertools.chain(*list(result_itertools)))

def rep_lengthout(x, lengthout=None,each=1):
    
    input=itertools.cycle(numpy.repeat(x, each))
    if lengthout:
        output=list(itertools.islice(itertools.cycle(input), lengthout))
    else:
        lengthout_all=len(x)*each
        output=list(itertools.islice(itertools.cycle(input), lengthout_all))
    return output


def rep_times_TF(x, times = 1, each = 1,index=[True]):
    x_index_TrueFalse=index_TF(x,index=index)
    ret_v=rep_times(x_index_TrueFalse, times=times,each=each)
    return(list(ret_v))

def rep_lengthout_TF(x, lengthout=None,each=1,index=[True]):
    x_index_TrueFalse=index_TF(x,index=index)
    output=rep_lengthout(x_index_TrueFalse, lengthout=lengthout,each=each)
    return output
  
rep_times_TF(lttrs, times = 2, each = 2,index=[True,False])
rep_lengthout_TF(lttrs, lengthout=None , each = 2,index=[True,False])
###########################################

#Example 1
#> rep(letters[1:3],times=c(1,2,4))
#[1] "a" "b" "b" "c" "c" "c" "c"
rd=numpy.repeat(lttrs,[1,2,4])
print(rd)
rep_times_TF(lttrs, times = 1, each = [1,2,4],index=[True])
##################################################


#Example 2
#> rep(letters[1:3],each=2,len=15)
# [1] "a" "a" "b" "b" "c" "c" "a" "a" "b" "b" "c" "c" "a" "a" "b"
#repeat a:c each element 2 until length be 15

input=itertools.cycle(numpy.repeat(lttrs, 2))
rd=list(itertools.islice(itertools.cycle(input), 15))
print(rd)

rep_lengthout_TF(lttrs, lengthout=15 , each = 2,index=[True])

###################################################



#Example 3
#> rep(letters[1:3],each=3,times=2)
# [1] "a" "a" "a" "b" "b" "b" "c" "c" "c" "a" "a" "a" "b" "b" "b" "c" "c" "c"
#repeat a:c each element 3  and repeat this 2 times

result_numpy=numpy.repeat(lttrs,3)
result_itertools=list(itertools.repeat(result_numpy,2))
rd= list(itertools.chain(*list(result_itertools)))
print(rd)

rep_times_TF(lttrs, times = 2, each = 3,index=[True])


######################################################


#Example 4
#> rep(letters[c(TRUE,FALSE)],each=2)
# [1] "a" "a" "c" "c" "e" "e" "g" "g" "i" "i" "k" "k" "m" "m" "o" "o" "q" "q" "s" "s" "u" "u"
#[23] "w" "w" "y" "y"

lttrs_TF=index_TF(letters,[True,False])
input=numpy.repeat(lttrs_TF, 2)
rd=list(input)
print(rd)

rep_times_TF(letters, times = 1, each = 2,index=[True,False])

#####################################
#Example 5
#> rep(letters[c(TRUE,FALSE,TRUE,FALSE,FALSE)],each=2)
# [1] "a" "a" "c" "c" "f" "f" "h" "h" "k" "k" "m" "m" "p" "p" "r" "r" "u" "u" "w" "w" "z" "z"
lttrs_TF=index_TF(letters,[True,False,True,False,False])
input=numpy.repeat(lttrs_TF, 2)
rd=list(input)
print(rd)

rep_times_TF(letters, times = 1, each = 2,index=[True,False,True,False,False])

#Example 6
#> rep(letters[c(TRUE,FALSE,TRUE,FALSE,FALSE)],each=2,len=25)
#[1] "a" "a" "c" "c" "f" "f" "h" "h" "k" "k" "m" "m" "p" "p" "r" "r" "u" "u" "w" "w" "z" "z"
#[23] "a" "a" "c"
lttrs_TF=index_TF(letters,[True,False,True,False,False])
input=itertools.cycle(numpy.repeat(lttrs_TF, 2))
output=list(itertools.islice(itertools.cycle(input), 25))
print(output)



rep_lengthout_TF(letters, lengthout=25 , each = 2,index=[True,False,True,False,False])
