class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        read_idx = 0
        write_idx = 0
        length = len(chars)
        
        while read_idx < length:
            char = chars[read_idx]
            count = 0
            
            while (read_idx < length and chars[read_idx] == char):
                count += 1
                read_idx += 1
                
            chars[write_idx] = char
            write_idx += 1
            
            if count > 1:
                for c in str(count):
                    chars[write_idx] = c
                    write_idx += 1
                    
        return write_idx

        
        