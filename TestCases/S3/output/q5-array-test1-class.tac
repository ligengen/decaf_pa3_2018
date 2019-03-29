VTABLE(_A) {
    <empty>
    A
    _A.seta;
    _A.printA;
}

VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_A_New) {
memo ''
_A_New:
    _T3 = 8
    parm _T3
    _T4 =  call _Alloc
    _T5 = 0
    *(_T4 + 4) = _T5
    _T6 = VTBL <_A>
    *(_T4 + 0) = _T6
    return _T4
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T7 = 4
    parm _T7
    _T8 =  call _Alloc
    _T9 = VTBL <_Main>
    *(_T8 + 0) = _T9
    return _T8
}

FUNCTION(_A.seta) {
memo '_T0:4 _T1:8'
_A.seta:
    _T10 = *(_T0 + 4)
    *(_T0 + 4) = _T1
}

FUNCTION(_A.printA) {
memo '_T2:4'
_A.printA:
    _T11 = *(_T2 + 4)
    parm _T11
    call _PrintInt
    _T12 = "\n"
    parm _T12
    call _PrintString
}

FUNCTION(main) {
memo ''
main:
    _T15 =  call _A_New
    _T14 = _T15
    _T16 = 10
    parm _T14
    parm _T16
    _T17 = *(_T14 + 0)
    _T18 = *(_T17 + 8)
    call _T18
    _T19 = 6
    _T20 = 0
    _T21 = (_T19 < _T20)
    if (_T21 == 0) branch _L13
    _T22 = "Decaf runtime error: The length of the created array should not be less than 0.\n"
    parm _T22
    call _PrintString
    call _Halt
_L13:
    _T23 = 4
    _T24 = (_T23 * _T19)
    _T25 = (_T23 + _T24)
    parm _T25
    _T26 =  call _Alloc
    *(_T26 + 0) = _T19
    _T26 = (_T26 + _T25)
_L14:
    _T25 = (_T25 - _T23)
    if (_T25 == 0) branch _L15
    _T26 = (_T26 - _T23)
    _T27 = 8
    parm _T27
    _T28 =  call _Alloc
    _T29 = *(_T14 + 4)
    *(_T28 + 4) = _T29
    _T30 = VTBL <_A>
    *(_T28 + 0) = _T30
    *(_T26 + 0) = _T28
    branch _L14
_L15:
    _T13 = _T26
    _T31 = 1
    _T32 = *(_T13 - 4)
    _T33 = (_T31 < _T32)
    if (_T33 == 0) branch _L16
    _T34 = 0
    _T35 = (_T31 < _T34)
    if (_T35 == 0) branch _L17
_L16:
    _T36 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T36
    call _PrintString
    call _Halt
_L17:
    _T37 = 4
    _T38 = (_T31 * _T37)
    _T39 = (_T13 + _T38)
    _T40 = *(_T39 + 0)
    _T41 = 15
    parm _T40
    parm _T41
    _T42 = *(_T40 + 0)
    _T43 = *(_T42 + 8)
    call _T43
    _T44 = 0
    _T45 = *(_T13 - 4)
    _T46 = (_T44 < _T45)
    if (_T46 == 0) branch _L18
    _T47 = 0
    _T48 = (_T44 < _T47)
    if (_T48 == 0) branch _L19
_L18:
    _T49 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T49
    call _PrintString
    call _Halt
_L19:
    _T50 = 4
    _T51 = (_T44 * _T50)
    _T52 = (_T13 + _T51)
    _T53 = *(_T52 + 0)
    parm _T53
    _T54 = *(_T53 + 0)
    _T55 = *(_T54 + 12)
    call _T55
    _T56 = 1
    _T57 = *(_T13 - 4)
    _T58 = (_T56 < _T57)
    if (_T58 == 0) branch _L20
    _T59 = 0
    _T60 = (_T56 < _T59)
    if (_T60 == 0) branch _L21
_L20:
    _T61 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T61
    call _PrintString
    call _Halt
_L21:
    _T62 = 4
    _T63 = (_T56 * _T62)
    _T64 = (_T13 + _T63)
    _T65 = *(_T64 + 0)
    parm _T65
    _T66 = *(_T65 + 0)
    _T67 = *(_T66 + 12)
    call _T67
}

