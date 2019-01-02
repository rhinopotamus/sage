r"""
PARI Groups

See :pari:`polgalois` for the PARI documentation of these objects.
"""

from sage.libs.pari import pari
from sage.rings.all import Integer
from sage.groups.perm_gps.permgroup_named import TransitiveGroup


class PariGroup(object):
    def __init__(self, x, degree):
        """
        EXAMPLES::

            sage: PariGroup([6, -1, 2, "S3"], 3)
            PARI group [6, -1, 2, S3] of degree 3
            sage: R.<x> = PolynomialRing(QQ)
            sage: f = x^4 - 17*x^3 - 2*x + 1
            sage: G = f.galois_group(pari_group=True); G
            PARI group [24, -1, 5, "S4"] of degree 4
        """
        self.__x = pari(x)
        self.__degree = Integer(degree)

    def __repr__(self):
        return "PARI group %s of degree %s" % (self.__x, self.__degree)

    def __eq__(self, other):
        """
        Test equality.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(QQ)
            sage: f1 = x^4 - 17*x^3 - 2*x + 1
            sage: f2 = x^3 - x - 1
            sage: G1 = f1.galois_group(pari_group=True)
            sage: G2 = f2.galois_group(pari_group=True)
            sage: G1 == G1
            True
            sage: G1 == G2
            False
        """
        return (isinstance(other, PariGroup) and
            (self.__x, self.__degree) == (other.__x, other.__degree))

    def __ne__(self, other):
        """
        Test inequality.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(QQ)
            sage: f1 = x^4 - 17*x^3 - 2*x + 1
            sage: f2 = x^3 - x - 1
            sage: G1 = f1.galois_group(pari_group=True)
            sage: G2 = f2.galois_group(pari_group=True)
            sage: G1 != G1
            False
            sage: G1 != G2
            True
        """
        return not (self == other)

    def __pari__(self):
        """
        TESTS::

            sage: G = PariGroup([6, -1, 2, "S3"], 3)
            sage: pari(G)
            [6, -1, 2, S3]
        """
        return self.__x

    def degree(self):
        """
        Return the degree of ``self``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(QQ)
            sage: f1 = x^4 - 17*x^3 - 2*x + 1
            sage: G1 = f1.galois_group(pari_group=True)
            sage: G1.degree()
            4
        """
        return self.__degree

    def order(self):
        """
        Return the order of ``self``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(QQ)
            sage: f1 = x^4 - 17*x^3 - 2*x + 1
            sage: G1 = f1.galois_group(pari_group=True)
            sage: G1.order()
            24
        """
        return Integer(self.__x[0])

    cardinality = order

    def permutation_group(self):
        return TransitiveGroup(self.__degree, self.__x[2])

    _permgroup_ = permutation_group
