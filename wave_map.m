function [ wave_map ] = wave_map(levels)
%WAVE_MAP Summary of this function goes here
%   Detailed explanation goes here

m_vec = linspace(0,1,levels)';

sigma_white = 0.022; % controls the sharpness of the transition fom yellow to blue,
sigma_color = 0.15; % controls the amount of purple and the fading from yellow to blue
fpos = 1/5;

red_line = heaviside(1/3-m_vec).*(0.3+0.7*3*m_vec) ...
    + heaviside(m_vec-1/3) - heaviside(m_vec-1/2) ...
    + heaviside(m_vec-1/2).*exp(-(m_vec-1/2).^2/(2*sigma_white^2) ) ...
    + 0.45*(1-fpos-m_vec>0).*exp(-(m_vec-1+fpos).^2/(2*sigma_color^2) ) ... % do not use heaviside, singular when argument = 0
    + 0.45*(m_vec-1+fpos>0).*exp(-(m_vec-1+fpos).^2/(2*sigma_color^2) ); % do not use heaviside, singular when argument = 0

green_line = heaviside(1/2-m_vec).*exp(-(m_vec-1/2).^2/(2*sigma_color^2) ) ...
    + heaviside(m_vec-1/2).*exp(-(m_vec-1/2).^2/(2*sigma_color^2) );

blue_line = heaviside(1/2-m_vec).*exp(-(m_vec-1/2).^2/(2*sigma_white^2) ) ...
    + heaviside(m_vec-1/2) - heaviside(m_vec-2/3) ...
    + heaviside(m_vec-2/3).*(1 + 3*0.7*(2/3-m_vec));

wave_map = flipud([red_line,green_line,blue_line]);
wave_map = min(wave_map,1);

% figure
% rgbplot(wave_map)
% 
% figure
% pcolor(peaks)
% colormap(wave_map)

end

