import numpy, itertools, string
letters =string.ascii_lowercase
letters =list(letters)
def rep_times(x, times=1,each=1):
    result_numpy=numpy.repeat(x,each)
    result_itertools=list(itertools.repeat(result_numpy,times))
    return list(itertools.chain(*list(result_itertools)))

#Example 1
#> rep(letters[1:3],times=c(1,2,4))
#[1] "a" "b" "b" "c" "c" "c" "c"
lttrs=[letters[i] for i in [0,1,2]]
print(lttrs)
rd=rep_times(lttrs,times=1, each=[1,2,3])
print(rd)

#Example 3
#> rep(letters[1:3],each=3,times=2)
# [1] "a" "a" "a" "b" "b" "b" "c" "c" "c" "a" "a" "a" "b" "b" "b" "c" "c" "c"
#repeat a:c each element 3  and repeat this 2 times
#Example 4
rd=rep_times(lttrs,times=2, each=3)
print(rd)


########################################

 

#Example 2
#> rep(letters[1:3],each=2,len=15)
# [1] "a" "a" "b" "b" "c" "c" "a" "a" "b" "b" "c" "c" "a" "a" "b"
#repeat a:c each element 2 until length be 15

def rep_lengthout(x, lengthout=None,each=1):
    import numpy, itertools
    input=itertools.cycle(numpy.repeat(x, each))
    if lengthout:
        output=list(itertools.islice(itertools.cycle(input), lengthout))
    else:
        output=list(input)
    return output
rd=rep_lengthout(lttrs, each=2,lengthout=15)
print(rd)


#Example 4
#> rep(letters[c(TRUE,FALSE)],each=2)
# [1] "a" "a" "c" "c" "e" "e" "g" "g" "i" "i" "k" "k" "m" "m" "o" "o" "q" "q" "s" "s" "u" "u"
#[23] "w" "w" "y" "y"


def which_is_true(indexTF):
    return [i for i, x in enumerate(indexTF) if x]
def index_TF(x,index=[True]):
    if(len(index)<len(x)):
        index_final=list(itertools.islice(itertools.cycle(index), len(x)))
    else:
        index_final=index[:len(x)]
    return [x[i] for i in list(which_is_true(index_final))]


def rep_times_TF(x, times=1,each=1,index=[True]):
    x_TF=list(index_TF(x,index))
    output=rep_times(x_TF, times=times,each=each)
    return list(output)

rd=rep_lengthout_TF(letters,lengthout=None,each=1,index=[True])
print(rd)

def rep_lengthout_TF(x,lengthout=None,each=1,index=[True]):
    x_TF=list(index_TF(x,index))
    output=rep_lengthout(x_TF, lengthout=lengthout,each=each)
    return list(output)

rd=rep_lengthout_TF(letters,lengthout=None,each=1,index=[True])
print(rd)
