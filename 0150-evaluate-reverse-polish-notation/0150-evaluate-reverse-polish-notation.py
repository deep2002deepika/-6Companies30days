class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        r=0
        l=0
        #l=tokens.split()
        for i in tokens:
            if i not in '+-/*':
                st.append(int(i))
            else:
                r=st.pop()
                l=st.pop()
                if i=='+':
                    st.append(int(l+r))
                elif i=='-':
                    st.append(int(l-r))
                elif i=='*':
                    st.append(int(l*r))
                else :
                    st.append(int(l/r))
                    
        return st.pop()
                
        