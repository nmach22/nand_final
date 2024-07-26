// ['8/FunctionCalls/FibonacciElement/Sys.vm', '8/FunctionCalls/FibonacciElement/Main.vm']
@256
D=A
@SP
M=D

// Function Sys.init
@RETURN_ADDRESS_Sys.init_0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL
@LCL
D=M
@SP
AM=M+1
A=A-1
M=D
// push ARG
@ARG
D=M
@SP
AM=M+1
A=A-1
M=D
// push THIS
@THIS
D=M
@SP
AM=M+1
A=A-1
M=D
// push THAT
@THAT
D=M
@SP
AM=M+1
A=A-1
M=D
// ARG = SP - 5 - nArgs
@SP
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// Jump
@Sys.init
0;JMP
// Define retAddr
(RETURN_ADDRESS_Sys.init_0)

// function Sys.init 0
(Sys.init)

// push constant 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1

// call Main.fibonacci 1
// Function Main.fibonacci
@RETURN_ADDRESS_Main.fibonacci_1
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL
@LCL
D=M
@SP
AM=M+1
A=A-1
M=D
// push ARG
@ARG
D=M
@SP
AM=M+1
A=A-1
M=D
// push THIS
@THIS
D=M
@SP
AM=M+1
A=A-1
M=D
// push THAT
@THAT
D=M
@SP
AM=M+1
A=A-1
M=D
// ARG = SP - 5 - nArgs
@SP
D=M
@1
D=D-A
@5
D=D-A
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// Jump
@Main.fibonacci
0;JMP
// Define retAddr
(RETURN_ADDRESS_Main.fibonacci_1)


// label END
(END)

// goto END
@END
0;JMP

// function Main.fibonacci 0
(Main.fibonacci)

// push argument 0
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
@LESS_TRUE_2
D;JLT
@SP
A=M-1
M=0
@LESS_END_2
0;JMP
(LESS_TRUE_2)
@SP
A=M-1
M=-1
(LESS_END_2)

// if-goto N_LT_2
@SP
AM=M-1
D=M
@N_LT_2
D;JNE

// goto N_GE_2
@N_GE_2
0;JMP

// label N_LT_2
(N_LT_2)

// push argument 0
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// return
//retAddr = *(LCL - 5)
@LCL
D=M
@5
A=D-A
D=M
@retAddr
M=D
// *ARG = pop()
@SP
A=M-1
D=M
@ARG
A=M
M=D
// SP = ARG + 1
@ARG
D=M+1
@SP
M=D
// THAT = *(LCL - 1)
@LCL
A=M-1
D=M
@THAT
M=D
// THIS = *(LCL - 2)
@2
D=A
@LCL
A=M-D
D=M
@THIS
M=D
// ARG = *(LCL - 3)
@3
D=A
@LCL
A=M-D
D=M
@ARG
M=D
// LCL = *(LCL - 4)
@4
D=A
@LCL
A=M-D
D=M
@LCL
M=D
@retAddr
A=M
0;JMP

// label N_GE_2
(N_GE_2)

// push argument 0
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D

// call Main.fibonacci 1
// Function Main.fibonacci
@RETURN_ADDRESS_Main.fibonacci_3
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL
@LCL
D=M
@SP
AM=M+1
A=A-1
M=D
// push ARG
@ARG
D=M
@SP
AM=M+1
A=A-1
M=D
// push THIS
@THIS
D=M
@SP
AM=M+1
A=A-1
M=D
// push THAT
@THAT
D=M
@SP
AM=M+1
A=A-1
M=D
// ARG = SP - 5 - nArgs
@SP
D=M
@1
D=D-A
@5
D=D-A
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// Jump
@Main.fibonacci
0;JMP
// Define retAddr
(RETURN_ADDRESS_Main.fibonacci_3)


// push argument 0
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D

// call Main.fibonacci 1
// Function Main.fibonacci
@RETURN_ADDRESS_Main.fibonacci_4
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL
@LCL
D=M
@SP
AM=M+1
A=A-1
M=D
// push ARG
@ARG
D=M
@SP
AM=M+1
A=A-1
M=D
// push THIS
@THIS
D=M
@SP
AM=M+1
A=A-1
M=D
// push THAT
@THAT
D=M
@SP
AM=M+1
A=A-1
M=D
// ARG = SP - 5 - nArgs
@SP
D=M
@1
D=D-A
@5
D=D-A
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// Jump
@Main.fibonacci
0;JMP
// Define retAddr
(RETURN_ADDRESS_Main.fibonacci_4)


// add
@SP
AM=M-1
D=M
A=A-1
M=M+D

// return
//retAddr = *(LCL - 5)
@LCL
D=M
@5
A=D-A
D=M
@retAddr
M=D
// *ARG = pop()
@SP
A=M-1
D=M
@ARG
A=M
M=D
// SP = ARG + 1
@ARG
D=M+1
@SP
M=D
// THAT = *(LCL - 1)
@LCL
A=M-1
D=M
@THAT
M=D
// THIS = *(LCL - 2)
@2
D=A
@LCL
A=M-D
D=M
@THIS
M=D
// ARG = *(LCL - 3)
@3
D=A
@LCL
A=M-D
D=M
@ARG
M=D
// LCL = *(LCL - 4)
@4
D=A
@LCL
A=M-D
D=M
@LCL
M=D
@retAddr
A=M
0;JMP

