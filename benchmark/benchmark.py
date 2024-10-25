import time
import sys
import dis
class Benchmark():
    '''
    Reusable class with benchmark information
    '''
    @staticmethod
    def show_objects(scope:dict):
        '''
        Show a table with informations about all the objects\n
        ---------------Input---------------------------------------------\n
        globals().copy() -> global objects\n
        locals().copy() -> local objects\n
        ---------------Input---------------------------------------------\n
        for locals(), use this method inside the scope that you want to analyze\n
        --------------Example--------------------------------------------\n
        Benchmark.show_objects(globals().copy()) -> print(global objects)\n
        --------------Example--------------------------------------------
        '''
        print('-' * 65)
        print(f"{'Name':<20} | {'Type':<20} | {'Value':<20}")
        print('-' * 65)
        for k,v in scope.items(): # dict com os nomes dos objetos e o tipo deles
            if k.startswith('__'):
                continue
            name = type(v).__name__
            value = str(v)
            if len(value) > 19:
                value = value[:16] + '...'
            if len(k) > 19:
                k = k[:16] + '...'
            print(f"{k:<20} | {name:<20} | {value:<20}")
    @staticmethod
    def variables_info(scope:dict):
        '''
        Show basic info about variables and mesure the size of them\n
        ---------------Input---------------------------------------------\n
        globals().copy() -> global variables\n
        locals().copy() -> local variables\n
        ---------------Input---------------------------------------------\n
        for locals(), use this method inside the scope that you want to analyze\n
        --------------Example--------------------------------------------\n
        Benchmark.variables_info(globals().copy()) -> print(global variables)\n
        --------------Example--------------------------------------------
        '''
        print('-' * 80)
        print(f"{'Name':<20} | {'Type':<20} | {'Value':<20} | {'Size':<20}")
        print('-' * 80)
        for k,v in scope.items():
            if k.startswith('__'):
                continue
            value = str(v)
            if not value.startswith("<"): # only variables
                tipo = type(v).__name__
                tamanho = sys.getsizeof(v)
                if isinstance(v,(list,tuple,set,dict)): # iterate over objects
                    if not isinstance(v,dict): # key-value pair
                        for each in v:
                            tamanho += sys.getsizeof(each)
                    else:
                        for k2,v2 in v.items():
                            tamanho += sys.getsizeof(k2) + sys.getsizeof(v2)
                print(f"{k:<20} | {tipo:<20} | {value:<20} | {tamanho} Bytes")
    @staticmethod
    def get_variables(scope:dict)->list:
        '''
        Returns a list with the scope's variables\n
        globals().copy() -> [global variables]\n
        locals().copy() -> [local variables]\n
        '''
        variables:list = []
        for k,v in scope.items():
            if k.startswith('__'):
                continue
            if isinstance(v,(int,float,complex,bool,str,list,tuple,set,dict)):
                variables.append(k)
        return variables
    @staticmethod
    def get_functions(scope:dict)->list:
        '''
        Returns a list with the scope's functions\n
        globals().copy() -> [global functions]\n
        locals().copy() -> [local functions]\n
        '''
        functions:list = []
        for k,v in scope.items():
            if str(v).startswith('<function'):
                functions.append(k)
        return functions
    @staticmethod
    def disassemble_function(func) -> None:
        '''
        Shows a representation of bytecode after the interpreter's optimizations
        '''
        instructions = 0
        bytecode = dis.Bytecode(func)
        print(f"{38*'-'}Bytecode{38*'-'}")
        for each in bytecode:
            instructions += 1
            instruction_name = each.opname
            instruction_arg = each.argrepr
            print(f"{instructions} | {instruction_name} {instruction_arg}")
        
        print(f"{38*'-'}Bytecode{38*'-'}")
        
def mesure_time(fun):
    '''
    Decorator that shows the time of execution of any function
    '''
    def wrapper():
        t0 = time.time()
        fun()
        tf = time.time()
        print(f"{tf-t0:.5f}s")
    return wrapper

def checkevents(fun):
    '''
    Decorator that executes a function and logs the steps for manual debugging
    '''
    def wrapper():
        def tracer(frame,event,arg):
            match(event):
                case 'call':  print(f"Start of {frame.f_code.co_name}")
                case 'line':  print(f"Line |{frame.f_lineno}")
                case 'return':  print(f"End of {frame.f_code.co_name}")
            return tracer
        sys.settrace(tracer)
        fun()
        sys.settrace(None)
    return wrapper

# criar função que executa o código inteiro sem saída no terminal e diz os passos que o programa tomou