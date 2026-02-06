import yaml


with open("data.yml", "r") as file:
    data = yaml.safe_load(file)


with open("REPORT.md", "w") as report:
    report.write(f"# {data['report']['title']}\n\n")
    report.write(f"**Generated for:** {data['report']['generated_for']}\n\n")
    report.write(f"**Environment:** {data['report']['environment']}\n\n")

    report.write("## Components\n\n")

    for component in data["components"]:
        report.write(f"### {component['name']}\n")
        report.write(f"- **Status:** {component['status']}\n")
        report.write(f"- **Owner:** {component['owner']}\n")
        report.write(f"- **Notes:** {component['notes']}\n\n")

print("REPORT.md generated successfully.")
