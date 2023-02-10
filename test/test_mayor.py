from mayor import Mayor as m 

class TestMayor:

    def test_mayor1(self):
        assert m.mayor(self,2,1) == 2
        
    def test_mayor2(self): 
        assert m.mayor(self,1,2) == 2
        
    def test_mayor3(self):   
        assert m.mayor(self,2,2) == None