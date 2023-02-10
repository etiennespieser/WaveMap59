function [] = paraview_color_space(RGBcolors, scheme)
% script modified from: https://www.paraview.org/Wiki/Manually_Creating_a_Colormap

N = length(RGBcolors);
fid = fopen([scheme '.xml'], 'w');
fprintf(fid, '<ColorMap name="%s" space="HSV">\n', scheme);
for i=1:N
    x = [(i-1)/(N-1); RGBcolors(i,:)'];
    fprintf(fid, '  <Point x="%f" o="1" r="%f" g="%f" b="%f"/>\n', x);
end
fwrite(fid, '</ColorMap>');
fclose(fid);
end
