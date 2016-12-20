function plt_dots = normalize_plot(Z, P, N)
  % Нормализация и построение точек
  for i=1:N
    Z(i) = Z(i)/P;
    if i > 1
      plot(Z(i-1), Z(i), '.r');
      hold on;
    end
  end
  axis([0 1 0 1]);
  set(get(gca,'XLabel'),'String','Z(i-1)');
  set(get(gca,'YLabel'),'String','Z(i)');
end
