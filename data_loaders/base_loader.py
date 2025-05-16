from abc import ABC, abstractmethod  # Import ABC tools for defining abstract classes.

# Define an abstract base class for data loaders
class DataLoader(ABC):
    # Abstract method, must be implemented by all subclasses
    @abstractmethod
    def load_data(self, filepath):
        pass  # No implementation here, subclasses will provide one
