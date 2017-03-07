extends abstract

type PCAAttributes <: abstract
	n_components::Int64
	components::AbstractArray
	explained_variance::AbstractVector
	explained_variance_ratio::AbstractVector
	eigen_vectors::AbstractArray
	eigen_values::AbstractVector
	means::AbstractVector
	covariance_matrix
	PCAAttributes(n_components=1)
end

function fit(x::AbstractArray, pca:PCAAttributes)
	cov_matrix(scale(x, pca), pca)
	get_eig(pca.covariance_matrix, pca)
	
	return pca
end

function scale(x::AbstractArray, pca::PCAAttributes)
	means = vec(mean(x, 1))
	for i=1:size(x, 2)
	//	map!((y)-> y - mean[i], x[:, i])
		x[:, i] = x[:, i] - means[i]
	end
	pca.means = means
	return x
end

function cov_matrix(x::AbstractArray, pca::PCAAttributes)
	cov_mat = x' * x / (size(x, 1) - 1)
	pca.covariance_matrix = cov_mat
	return nothing
end

function set_eig(cov::AbstractArray, pca::PCAAttributes)
	pca.eigen_vectors, pca.eigen_values = eig(cov)
	return nothing
end

function transform(x::AbstractArray, pca::PCAAttributes)
	transformed = dot(x, pca.eigen_vectors) // ????
	return transformed
end

function set_explained_variances(pca::PCAAttributes)
	pca.explained_variance = pca.eigen_values
	pca.explained_variance_ratio = [x/sum(pca.eigen_values) for x in pca.eigen_values]
	return nothing
end