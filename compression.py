class AlgorithmBuilding():
    def __init__(self,binary):
        self.binary = binary
    def runAlgorithm(self):
        image = self.binary
        compressed_image = []
        original_size = 0
        compressed_size = 0

        for i in range(0, image.shape[0]):
            current_value = image[i][0]
            current_count = 0
            curr = []
            for j in range(0, len(image[0])):
                original_size += 1
                if image[i][j] == current_value:
                    current_count += 1
                else:
                    curr.append([int(current_value), int(current_count)])
                    compressed_size += 1 + (current_count > 1) # 1 for the value, and an additional byte if the count is more than 1
                    current_value = image[i][j]
                    current_count = 1
            curr.append([int(current_value), int(current_count)])
            compressed_image.append(curr)

        compression_ratio =  original_size/compressed_size
        print("Original size is ", original_size)
        print("Compressed size is ", compressed_size)

        return [compressed_image,compression_ratio]
        