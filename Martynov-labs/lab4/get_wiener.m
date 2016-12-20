function [t w] = get_wiener(n, dim)
    % в зависимости от размерности генерируем либо 
    % одномерный процесс, либо двумерный
    if dim == 1
        [w t] = calc_wiener(n);
    else if dim == 2
        [t, ] = calc_wiener(n);
        [w, ] = calc_wiener(n);
    end
end
