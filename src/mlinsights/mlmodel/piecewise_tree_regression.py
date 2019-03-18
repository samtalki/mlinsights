# -*- coding: utf-8 -*-
"""
@file
@brief Implémente une régression linéaire par morceaux en modifiant
l'algorithme de construction des arbres de décision.
"""
from sklearn.tree import DecisionTreeRegressor
from .piecewise_tree_regression_criterion import SimpleRegressorCriterion  # pylint: disable=E0611


class DecisionTreeLinearRegressor(DecisionTreeRegressor):
    """
    Réécrit le critère qui permet d'optimiser
    la construction de l'arbre.
    Voir :epkg:`sklearn:tree:DecisionTreeRegressor` pour les paramètres.
    """

    def __init__(self, criterion='mselin', splitter='best', max_depth=None,
                 min_samples_split=2, min_samples_leaf=1,
                 min_weight_fraction_leaf=0.0, max_features=None,
                 random_state=None, max_leaf_nodes=None,
                 min_impurity_decrease=0.0, min_impurity_split=None,
                 presort=False):
        DecisionTreeRegressor.__init__(self, criterion=criterion,
                                       splitter=splitter, max_depth=max_depth,
                                       min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf,
                                       min_weight_fraction_leaf=min_weight_fraction_leaf, max_features=max_features,
                                       random_state=random_state, max_leaf_nodes=max_leaf_nodes,
                                       min_impurity_decrease=min_impurity_decrease, min_impurity_split=min_impurity_split,
                                       presort=presort)

    def fit(self, X, y, sample_weight=None, check_input=True,
            X_idx_sorted=None):
        """
        Réinterprète le paramètre *criterion*.
        """
        if self.criterion == 'mselin':
            # self.criterion = LinearRegressionCriterion(X, y, sample_weight)
            replace = True
            raise NotImplementedError()
        elif self.criterion == "simple":
            self.criterion = SimpleRegressorCriterion(X, y, sample_weight)
        else:
            replace = False

        self.fit(X, y, sample_weight=sample_weight, check_input=check_input,
                 X_idx_sorted=X_idx_sorted)

        if replace:
            self.criterion = 'mselin'
        return self