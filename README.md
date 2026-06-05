local function ExibirAvisoManutencao()
    local ScreenGui = Instance.new("ScreenGui", (gethui and gethui()) or game:GetService("CoreGui"))
    local Frame = Instance.new("Frame", ScreenGui)
    Frame.Size = UDim2.new(0, 300, 0, 150)
    Frame.Position = UDim2.new(0.5, -150, 0.5, -75)
    Frame.BackgroundColor3 = Color3.fromRGB(20, 20, 20)
    Instance.new("UICorner", Frame).CornerRadius = UDim.new(0, 8)
    
    local Text = Instance.new("TextLabel", Frame)
    Text.Size = UDim2.new(1, 0, 1, 0)
    Text.Text = "⚠️ MANUTENÇÃO\n\nO NIGHT-FFH4X está em manutenção.\nPor favor, aguarde o retorno."
    Text.TextColor3 = Color3.fromRGB(255, 255, 255)
    Text.Font = Enum.Font.GothamBold
    Text.TextSize = 16
    Text.BackgroundTransparency = 1
    
    task.wait(5) -- O aviso some após 5 segundos
    ScreenGui:Destroy()
end

-- lop
task.spawn(ExibirAvisoManutencao)
