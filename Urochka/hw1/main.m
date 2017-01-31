clear all;

q = 1/pi;
M = 3/2;
N = 2000;

w = zeros(N, 2);
y = zeros(N, 2);

for i=1:N
    while (1)
        u = rand();
        theta = pi/2 * rand();
        phi = 2*pi * rand();
        j = get_jacobian(theta, phi);
        p = 1/16.655 * sqrt(j);

        if p/(M*q) >= u
            w(i, :) = [theta phi];
            break;
        end
    end

    y(i, :) = [pi/2 * rand() 2*pi * rand()];

end

plot_surface(w, y)
