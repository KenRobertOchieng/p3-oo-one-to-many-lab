class Pet:
  # Allowed pet types
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    # Cache all Pet instances
    all = []

    def __init__(self, name, pet_type, owner=None):
        # Validate pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet_type: {pet_type!r}")
        # Validate owner if provided
        if owner is not None:
            from owner_pet import Owner
            if not isinstance(owner, Owner):
                raise Exception("owner must be an Owner instance")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        # Register instance
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return a list of Pet instances belonging to this owner."""
        from owner_pet import Pet
        return [pet for pet in Pet.all if pet.owner is self]

    def add_pet(self, pet):
        """Associate a Pet instance with this owner."""
        from owner_pet import Pet
        if not isinstance(pet, Pet):
            raise Exception("add_pet expects a Pet instance")
        pet.owner = self
        return pet

    def get_sorted_pets(self):
        """Return this owner's pets sorted by name."""
        return sorted(self.pets(), key=lambda pet: pet.name)