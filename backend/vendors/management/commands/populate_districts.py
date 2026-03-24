from django.core.management.base import BaseCommand
from vendors.models import District, Subdistrict

class Command(BaseCommand):
    help = 'Populate districts and subdistricts of Bangladesh'

    def handle(self, *args, **kwargs):
        data = {
            'Jhenaidah' : ['Shailkupa', 'Jhenaidah Sadar', 'Harinakundu', 'Kaligonj', 'Kotchadpur', 'Maheshpur'],
            # 'Dhaka': ['Dhamrai', 'Dohar', 'Keraniganj', 'Nawabganj', 'Savar'],
            # 'Chittagong': ['Anwara', 'Banshkhali', 'Boalkhali', 'Chandanaish', 'Fatikchhari', 'Hathazari', 'Lohagara', 'Mirsharai', 'Patiya', 'Rangunia', 'Raozan', 'Sandwip', 'Satkania', 'Sitakunda'],
            # 'Rajshahi': ['Bagha', 'Bagmara', 'Charghat', 'Durgapur', 'Godagari', 'Mohanpur', 'Paba', 'Puthia', 'Tanore'],
            # 'Khulna': ['Batiaghata', 'Dacope', 'Dumuria', 'Dighalia', 'Koyra', 'Paikgacha', 'Phultala', 'Rupsa', 'Terokhada'],
            # 'Sylhet': ['Balaganj', 'Beanibazar', 'Bishwanath', 'Companiganj', 'Fenchuganj', 'Golapganj', 'Gowainghat', 'Jaintiapur', 'Kanaighat', 'Osmani Nagar', 'South Surma', 'Zakiganj'],
            # 'Barisal': ['Agailjhara', 'Babuganj', 'Bakerganj', 'Banaripara', 'Gaurnadi', 'Hizla', 'Mehendiganj', 'Muladi', 'Wazirpur'],
            # 'Rangpur': ['Badarganj', 'Gangachara', 'Kaunia', 'Mithapukur', 'Pirgacha', 'Pirganj', 'Taraganj'],
            # 'Mymensingh': ['Bhaluka', 'Dhobaura', 'Fulbaria', 'Gaffargaon', 'Gauripur', 'Haluaghat', 'Ishwarganj', 'Muktagacha', 'Nandail', 'Phulpur', 'Trishal'],
            # 'Comilla': ['Barura', 'Brahmanpara', 'Burichang', 'Chandina', 'Chauddagram', 'Daudkandi', 'Debidwar', 'Homna', 'Laksam', 'Lalmai', 'Meghna', 'Monohorgonj', 'Muradnagar', 'Nangalkot', 'Titas'],
            # 'Narayanganj': ['Araihazar', 'Bandar', 'Rupganj', 'Sonargaon'],
            # 'Gazipur': ['Gazipur Sadar', 'Kaliakair', 'Kaliganj', 'Kapasia', 'Sreepur'],
            # 'Tangail': ['Basail', 'Bhuapur', 'Delduar', 'Dhanbari', 'Ghatail', 'Gopalpur', 'Kalihati', 'Madhupur', 'Mirzapur', 'Nagarpur', 'Sakhipur'],
            # 'Jessore': ['Abhaynagar', 'Bagherpara', 'Chaugachha', 'Jhikargacha', 'Keshabpur', 'Manirampur', 'Sharsha'],
            # 'Bogra': ['Adamdighi', 'Dhunat', 'Dhupchanchia', 'Gabtali', 'Kahaloo', 'Nandigram', 'Sariakandi', 'Shajahanpur', 'Sherpur', 'Shibganj', 'Sonatala'],
            # 'Dinajpur': ['Birampur', 'Birganj', 'Biral', 'Bochaganj', 'Chirirbandar', 'Fulbari', 'Ghoraghat', 'Hakimpur', 'Kaharole', 'Khansama', 'Nawabganj', 'Parbatipur'],
        }

        for district_name, subdistricts in data.items():
            district, created = District.objects.get_or_create(name=district_name)
            if created:
                self.stdout.write(f'Created district: {district_name}')
            for subdistrict_name in subdistricts:
                Subdistrict.objects.get_or_create(name=subdistrict_name, district=district)
            self.stdout.write(f'Populated subdistricts for: {district_name}')

        self.stdout.write(self.style.SUCCESS('Successfully populated all districts and subdistricts!'))