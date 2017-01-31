function none = plot_surface(w, y)
    angle1 = pi/2;
    angle2 = 2*pi;

    [theta phi] = meshgrid(linspace(0, angle1, 30), linspace(0, angle2, 30));
    X = sqrt(3) .* sin(theta) .* cos(phi);
    Y = sqrt(2) .* sin(theta) .* sin(phi);
    Z = cos(theta);
    surf(X, Y, Z)

    hold on;

    plot3(sqrt(3) .* sin(w(:, 1)) .* cos(w(:, 2)), sqrt(2) .* sin(w(:, 1)) .* sin(w(:, 2)), cos(w(:, 1)), 'ob')
    plot3(sqrt(3) .* sin(y(:, 1)) .* cos(y(:, 2)), sqrt(2) .* sin(y(:, 1)) .* sin(y(:, 2)), cos(y(:, 1)), '+r')

    legend('By square', 'By params');
    alpha(0.7);
    xlabel('x')
    ylabel('y')
    zlabel('z')
    title('Surface and random points')
