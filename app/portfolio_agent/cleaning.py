def clean_skills_data(data: dict) -> dict:
    """
    Clean the general information about Faisal.
    """

    if not len(data.get("skills")) == 3 or not data.get("resume", {}).get("view_url"):
        return data

    cleaned_data = {}

    cleaned_data["resume_url"] = data["resume"].get("view_url", "")

    if cleaned_data["resume_url"]:
        cleaned_data["resume_url"] = cleaned_data["resume_url"].replace(
            "view", "preview"
        )

    cleaned_data["skills"] = []

    for item in zip(
        data["skills"][0].get("items", []),
        data["skills"][1].get("items", []),
        data["skills"][2].get("items", []),
    ):
        for i in item:
            cleaned_data["skills"].append(f"{i.get('name')} ({i.get('link')})")

    cleaned_data["types_of_works"] = [
        item.get("category", "") for item in data["skills"]
    ]
    return cleaned_data
