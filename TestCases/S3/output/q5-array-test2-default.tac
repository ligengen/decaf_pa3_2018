VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T0 = 4
    parm _T0
    _T1 =  call _Alloc
    _T2 = VTBL <_Main>
    *(_T1 + 0) = _T2
    return _T1
}

FUNCTION(main) {
memo ''
main:
    _T4 = 2
    _T5 = "pa1"
    _T6 = 0
    _T7 = (_T4 < _T6)
    if (_T7 == 0) branch _L10
    _T8 = "Decaf runtime error: The length of the created array should not be less than 0.\n"
    parm _T8
    call _PrintString
    call _Halt
_L10:
    _T9 = 4
    _T10 = (_T9 * _T4)
    _T11 = (_T9 + _T10)
    parm _T11
    _T12 =  call _Alloc
    *(_T12 + 0) = _T4
    _T12 = (_T12 + _T11)
_L11:
    _T11 = (_T11 - _T9)
    if (_T11 == 0) branch _L12
    _T12 = (_T12 - _T9)
    *(_T12 + 0) = _T5
    branch _L11
_L12:
    _T3 = _T12
    _T14 = 0
    _T15 = "pa2"
    _T16 = *(_T3 - 4)
    _T17 = (_T14 < _T16)
    if (_T17 == 0) branch _L13
    _T18 = 0
    _T19 = (_T14 < _T18)
    if (_T19 == 0) branch _L14
_L13:
    _T20 = 0
    _T20 = _T15
    branch _L15
_L14:
    _T21 = 4
    _T22 = (_T14 * _T21)
    _T23 = (_T3 + _T22)
    _T24 = *(_T23 + 0)
    _T20 = _T24
    branch _L15
_L15:
    _T13 = _T20
    _T26 = 2
    _T27 = "pa3"
    _T28 = *(_T3 - 4)
    _T29 = (_T26 < _T28)
    if (_T29 == 0) branch _L16
    _T30 = 0
    _T31 = (_T26 < _T30)
    if (_T31 == 0) branch _L17
_L16:
    _T32 = 0
    _T32 = _T27
    branch _L18
_L17:
    _T33 = 4
    _T34 = (_T26 * _T33)
    _T35 = (_T3 + _T34)
    _T36 = *(_T35 + 0)
    _T32 = _T36
    branch _L18
_L18:
    _T25 = _T32
    parm _T13
    call _PrintString
    parm _T25
    call _PrintString
}

