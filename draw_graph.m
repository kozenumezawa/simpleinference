data = csvread('./csv/inputdata.csv');

datasize = size(data);
N_DATA = datasize(1) / 2;   %   the number of X or Y
TIMESTEP = datasize(2);

t = [1:TIMESTEP];

X = zeros(N_DATA, TIMESTEP);
Y = zeros(N_DATA, TIMESTEP);

j = 1;
for i = 1:N_DATA
     X(i,:) = data(j,:);
     Y(i,:) = data(j+1,:);
     j = j + 2;
end

figure(1)
plot(t, X);

figure(2)
plot(t,Y);
 