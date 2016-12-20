function [t w] = get_wiener(n, dim)
    % � ����������� �� ����������� ���������� ���� 
    % ���������� �������, ���� ���������
    if dim == 1
        [w t] = calc_wiener(n);
    else if dim == 2
        [t, ] = calc_wiener(n);
        [w, ] = calc_wiener(n);
    end
end
