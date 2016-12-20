function didhit = throw_needle()
  needle_length = 1; % ����� ����
  xcoord = needle_length * rand(); % ������������� ������ ����, ����� ���� ��������� � ���� ����� ����� �������
  angle = 2*pi * rand(); % ������������� ���� ���� ����� �������
  % ���������� ���� �� ������ ���. ���� �����+��������/2 ������ 1 ��� �����+��������/2 ������ 0, ������ ���� �� �������
  projection = abs(needle_length/2 * sin(angle));
  if ((xcoord + projection) > needle_length) || ((xcoord - projection) < 0)
    didhit = 1;
  else
    didhit = 0;
  end
end
