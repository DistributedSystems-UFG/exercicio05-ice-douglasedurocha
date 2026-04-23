# -*- coding: utf-8 -*-
import Ice, IcePy

_M_Demo = Ice.openModule('Demo')
__name__ = 'Demo'

_M_Demo._t_Calculator = IcePy.defineValue('::Demo::Calculator', Ice.Value, -1, (), False, True, None, ())

if 'CalculatorPrx' not in _M_Demo.__dict__:
    _M_Demo.CalculatorPrx = Ice.createTempClass()
    class CalculatorPrx(Ice.ObjectPrx):

        def add(self, a, b, context=None):
            return _M_Demo.Calculator._op_add.invoke(self, ((a, b), context))

        def addAsync(self, a, b, context=None):
            return _M_Demo.Calculator._op_add.invokeAsync(self, ((a, b), context))

        def begin_add(self, a, b, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Calculator._op_add.begin(self, ((a, b), _response, _ex, _sent, context))

        def end_add(self, _r):
            return _M_Demo.Calculator._op_add.end(self, _r)

        def subtract(self, a, b, context=None):
            return _M_Demo.Calculator._op_subtract.invoke(self, ((a, b), context))

        def subtractAsync(self, a, b, context=None):
            return _M_Demo.Calculator._op_subtract.invokeAsync(self, ((a, b), context))

        def begin_subtract(self, a, b, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Calculator._op_subtract.begin(self, ((a, b), _response, _ex, _sent, context))

        def end_subtract(self, _r):
            return _M_Demo.Calculator._op_subtract.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Demo.CalculatorPrx.ice_checkedCast(proxy, '::Demo::Calculator', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Demo.CalculatorPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Demo::Calculator'
    _M_Demo._t_CalculatorPrx = IcePy.defineProxy('::Demo::Calculator', CalculatorPrx)

    _M_Demo.CalculatorPrx = CalculatorPrx
    del CalculatorPrx

    _M_Demo.Calculator = Ice.createTempClass()
    class Calculator(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Demo::Calculator', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Demo::Calculator'

        @staticmethod
        def ice_staticId():
            return '::Demo::Calculator'

        def add(self, a, b, current=None):
            raise NotImplementedError("servant method 'add' not implemented")

        def subtract(self, a, b, current=None):
            raise NotImplementedError("servant method 'subtract' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Demo._t_CalculatorDisp)

        __repr__ = __str__

    _M_Demo._t_CalculatorDisp = IcePy.defineClass('::Demo::Calculator', Calculator, (), None, ())
    Calculator._ice_type = _M_Demo._t_CalculatorDisp

    Calculator._op_add = IcePy.Operation('add', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 1)), (), IcePy._t_int, ())
    Calculator._op_subtract = IcePy.Operation('subtract', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 1)), (), IcePy._t_int, ())

    _M_Demo.Calculator = Calculator
    del Calculator