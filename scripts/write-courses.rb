require "erb"

for lang in [ "de", "fr" ] do
    filename = "../_includes/courstable-#{lang}.html"
    name1 = "hello world"
    template = File.read('./template.erb')
    rendered_template = ERB.new(template)

    File.open(filename, 'w') do |f|
        f.write rendered_template.result(binding)
        puts "... wrote #{filename}"
    end
end

