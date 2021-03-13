# class TSNE:
#     def __init__(self,
#                  perp=40,
#                  iter=100,
#                  lr=0.01,
#                  momentum=0.1,
#                  low_dim=2):
#
#     def fit(self, x):
#         # data에서 euclidean distance matrix를 구한다
#         distances = pairwise_distance(x) # pairwise_distances(x, metric=self.metric, squared=True)
#         P = _joint_probabilities(distances, self.perplexity, self.verbose)
#
#         # binary search, shannon entropy에 따라 1~n의 sigma를 구한 후 P matrix를 반환한다
#
#         # gradient descent 로 y를 구한다

import numpy as np

def pairwise_euclidean_distance_matrix(x):
    """make euclidean distance matrix.

    Parameters
    ----------
    x : ndarray of shape (n_samples, n_features)

    Returns
    -------
    matrix : ndarray of shape (n_samples, n_samples)

    Examples::
        x = np.random.randn(5, 784)
        distances = pairwise_euclidean_distance_matrix(x)
    """
    matrix = np.zeros((x.shape[0], x.shape[0]))
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if i != j:
                matrix[i][j] = np.sqrt(sum((x[i] - x[j]) ** 2))
    return matrix

def binary_search_using_perplexity(distances, perplexity=30):
    """use binary search & perplexity to make conditonal probability.

    Parameters
    ----------
    distances : ndarray of shape (n_samples, n_samples)
    perplexity : int = 30

    Returns
    -------
    conditional_p : ndarray of shape (n_samples, n_samples)

    Examples::
        perplexity = 3
        distances = pairwise_euclidean_distance_matrix(x)
        conditional_p = binary_search_perplexity(distances, perplexity)
    """
    n_samples = distances.shape[0]
    n_features = distances.shape[1]
    binary_search_steps = 30
    perplexity_threshold = 1e-5

    conditional_p = np.zeros_like(distances)
    for i in range(n_samples):
        binary_search_max_value = np.Infinity
        binary_search_min_value = -np.Infinity
        sigma_i = 1
        # binary search
        for step in range(binary_search_steps):
            sum_pi = 0
            for j in range(n_features):
                if i != j:
                    conditional_p[i, j] = np.exp(-distances[i, j] / sigma_i)
                    sum_pi += conditional_p[i, j]

            H = 0
            for j in range(n_features):
                if i != j:
                    conditional_p[i, j] /= sum_pi
                    H += conditional_p[i, j] * np.log2(conditional_p[i, j])

            current_entropy = 2 ** (-H)
            entropy_diff = current_entropy - perplexity

            # 종료조건
            if np.abs(entropy_diff) <= perplexity_threshold:
                break
            if entropy_diff > 0:
                # current_entropy는 작아져야 함 -> sigma_i가 작아져야 함
                binary_search_max_value = sigma_i
                if binary_search_min_value == -np.Infinity:
                    sigma_i /= 2
                else:
                    sigma_i = (sigma_i + binary_search_min_value) / 2
            else:
                # current_entropy는 커져야 함 -> sigma_i가 커져야 함
                binary_search_min_value = sigma_i
                if binary_search_max_value == np.Infinity:
                    sigma_i *= 2
                else:
                    sigma_i = (sigma_i + binary_search_max_value) / 2

    return conditional_p

def joint_probabilities(x, perplexity=30):
    """make joint probability.

        Parameters
        ----------
        x : ndarray of shape (n_samples, n_features)
        perplexity : int = 30

        Returns
        -------
        p : ndarray of shape (n_samples, n_samples)

        Examples::
            perplexity = 3
            x = np.random.randn(n_samples, dim)
            p = joint_probabilities(x, perplexity)
        """
    distances = pairwise_euclidean_distance_matrix(x)
    conditional_p = binary_search_using_perplexity(distances, perplexity)
    p = (conditional_p + conditional_p.T) / (2 * n_samples)
    return p

if __name__=="__main__":
    perplexity = 3
    n_samples = 70000
    dim = 784
    x = np.random.randn(n_samples, dim) # x = np.random.uniform(0, 1, n_samples*dim).reshape(n_samples, dim)
    p = joint_probabilities(x, perplexity)


    from sklearn.manifold import TSNE

